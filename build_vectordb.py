# build_vector_db.py
import json
import os
import torch
from typing import List
from langchain_core.documents import Document
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import shutil

"""
<필요 설치 모듈>
pip install langchain-core
pip install langchain-community
pip install langchain-chroma
pip install langchain-text-splitters
pip install sentence-transformers
pip install chromadb
pip3 install torch torchvision torchaudio # (권장) Apple Silicon/MPS 또는 CPU용 PyTorch
"""

# ── 0) 디바이스 자동 감지 (MPS → CUDA → CPU)
if torch.backends.mps.is_available():
    DEVICE_STR = "mps"
elif torch.cuda.is_available():
    DEVICE_STR = "cuda"
else:
    DEVICE_STR = "cpu"
print(f"[Device] Using: {DEVICE_STR}")

def load_jsonl(path: str) -> List[dict]:
    """jsonl 파일 불러오기"""
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def auto_chunk_for_qa(docs: List[Document]) -> List[Document]:
    """
    Q+A 모드에서만 사용.
    문서 길이를 보고 자동으로 청킹을 적용:
      - 최대 길이 <= 500자 → 분할 스킵
      - 그 외 → chunk_size=800, overlap=80 (≈10%)
    """
    if not docs:
        return docs

    lengths = [len(d.page_content) for d in docs]
    max_len = max(lengths)

    if max_len <= 500:
        # 현재 데이터가 짧은 Q/A 위주면 청킹 불필요
        print("✂️ Chunking: 스킵 (max_len <= 500)")
        return docs

    print(f"✂️ Chunking: 적용 (max_len={max_len}) → chunk_size=800, overlap=80")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,   #≈10%
        separators=["\n\n", "\n", "。", ".", "!", "?", " ", ""]
    )
    chunked = splitter.split_documents(docs)
    print(f"   ↳ {len(docs)}개 → {len(chunked)}개 청크로 분할 완료")
    return chunked


def build_vector_db(jsonl_path: str, persist_dir: str = "vector_store", mode: str = "qa"):
    """
    mode = "qa"     → Q + A를 page_content에 저장 (길면 자동 청킹)
    mode = "q_only" → Q만 page_content, A는 metadata에 저장 (청킹 없음)
    """
    print(f"\n🚀 VectorDB 구축 시작 | mode={mode}")
    print(f"📂 {jsonl_path} 불러오는 중...")
    records = load_jsonl(jsonl_path)
    print(f"✅ {len(records)}개 레코드 로드 완료")

    # 1) Document 변환
    print("📝 Document 변환 중...")
    docs: List[Document] = []
    for i, item in enumerate(records, 1):
        q = str(item.get("Q", "")).strip()
        a = str(item.get("A", "")).strip()

        if mode == "q_only":
            # 검색은 질문(Q) 기준, 답변(A)는 메타데이터로 보관
            docs.append(Document(page_content=q, metadata={"type": "Q-A", "answer": a}))
        else:
            # 기본: Q + A 합쳐서 저장 → 길면 아래서 자동 청킹
            docs.append(Document(page_content=f"Q: {q}\nA: {a}", metadata={"type": "Q-A", "question": q}))

        if i % 100 == 0:
            print(f"   ↳ {i}/{len(records)} 변환 완료")
    print("✅ Document 변환 완료")

    # 2) (Q+A 모드일 때만) 자동 청킹
    if mode == "qa":
        docs = auto_chunk_for_qa(docs)

    # 3) 임베딩 & 벡터DB 저장
    print("🔎 임베딩 모델 로딩 중... (nlpai-lab/KURE-v1)")
    embedding_model = SentenceTransformerEmbeddings(
        model_name="nlpai-lab/KURE-v1",
        model_kwargs={"device": DEVICE_STR},   # 여기서 디바이스 지정
        encode_kwargs={"batch_size": 64}       # 적절히 조정 가능
    )

    # 기존 DB 폴더 삭제 후 새로 생성
    if os.path.exists(persist_dir):
        #import shutil
        print(f"🗑 기존 DB({persist_dir}) 삭제 중...")
        shutil.rmtree(persist_dir)

    print(f"💾 Chroma 벡터스토어에 저장 중... → {persist_dir}")
    os.makedirs(persist_dir, exist_ok=True)
    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory=persist_dir
    )
    print(f"🎉 완료! 총 {len(docs)}개(청크 기준) 문서를 {persist_dir}에 저장했습니다. (mode={mode})")


# 이 블록은 파일을 직접 실행할 때만 실행됨
# 다른 모듈에서 import할 때는 실행되지 않아 DB가 자동 재생성되지 않음 (이럴 일은 사실 없음)
if __name__ == "__main__":
    # Q+A 방식 (자동 청킹)
    build_vector_db("data/combined_data.jsonl", persist_dir="vector_store_qa", mode="qa")

    # Q-only 방식 (청킹 없음)
    build_vector_db("data/combined_data.jsonl", persist_dir="vector_store_q_only", mode="q_only")