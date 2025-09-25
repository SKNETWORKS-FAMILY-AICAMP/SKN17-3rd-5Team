# SKN 17기 - 3rd Project 5Team 
> **주제** : LLM을 연동한 내외부 문서 기반 질의 응답 시스템  
  개발 기간: 2025.09.24 ~ 2025.09.25

---

# 🔖 목차 

<details>
<summary>목차 내용</summary>

#### 1. [팀 소개](#0️⃣-팀-소개)  
#### 2. [프로젝트 개요](#1️⃣-프로젝트-개요)  
#### 3. [기술 스택](#2️⃣-기술-스택)  
#### 4. [시스템 아키텍처](#3️⃣-시스템-아키텍쳐)  
#### 5. [WBS](#4️⃣-wbs)  
#### 6. [요구사항 명세서](#5️⃣-요구사항-명세서)  
#### 7. [수집한 데이터 및 전처리 요약](#6️⃣-수집한-데이터-및-전처리-요약)  
#### 8. [DB 연동 구현 코드](#7️⃣-db-연동-구현-코드)  
#### 9. [모델 선정 이유](#8️⃣-모델-선정-이유)  
#### 10. [테스트 계획 및 결과 보고서](#9️⃣-테스트-계획-및-결과-보고서)  
#### 11. [진행 과정 중 프로젝트 개선 노력](#🔟-진행-과정-중-프로젝트-개선-노력)  
#### 12. [수행 결과](#📜-수행-결과) 
#### 13. [프로젝트 결과 및 향후 계획](#📒-결과-정리-및-향후-계획)
#### 14. [한 줄 회고](#한-줄-회고)  

</details>

---

# 0️⃣ **팀 소개**
### **🔸팀명: 모빌리티 브레인**
> 교통 관련한 두뇌를 맡는다

### **🔸팀원 소개**
| [@임길진](https://github.com/LGJ0405)                      | [@박민정](https://github.com/minjeon)                       |  [@이가은](https://github.com/Leegaeune)                       | [@한 훈](https://github.com/Hoonieboogie)                       |
|---------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/dc864318-18e5-46c2-a11f-b0207c1eed96" />| <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/ba73c676-9539-4742-87ba-fe2a2436f453" />| <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/d9f7e063-5cc1-4804-a2ab-9a00b7d16ce4" />| <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/c31f1a82-d873-4963-9140-f31487f1faa5" /> |



---

# 1️⃣ **프로젝트 개요**
## **🔸프로젝트 명: 🚗A.D.A(AI Driving Assistant)🚗**
## **🔸프로젝트 소개**

**A.D.A(AI Driving Assistant)** 는 운전자들이 주행 중 맞닥뜨릴 수 있는 다양한 돌발 상황에 대해 실시간으로 대처법, 가이드, 안전 수칙을 제공하는 LLM 기반 챗봇입니다. 음성이나 텍스트로 질문하면 즉시 답변을 제공하여 운전자 스스로 빠르고 정확하게 대응할 수 있도록 돕습니다. 

## **🔸프로젝트 필요성**

| <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/03f97e35-3e32-40b7-a8b1-1383ab04765d" /> | <img width="822" height="500" alt="image" src="https://github.com/user-attachments/assets/e47ecf3f-6de8-41f2-bf94-b4bd96bf78ff" />|
|---------------------------|---------------------------|
| - 자동차 고장·사고 시 당황으로 인한 2차 사고 위험 <br><br> - 교통 사고 2차 사고 치사율은 일반 교통 사고의 약 6배에 달하는 54% <br><br> - "고속도로 한복판에서 시동 꺼진 차량, 운전자가 대처 방법 몰라 뒤따라오던 차량과 추돌" 과 같은 기사 자주 보도 <br><br> 출처 : ["고속도로 교통사고 사망자 5명 중 1명 2차 사고로 사망"](https://www.yna.co.kr/view/AKR20240319052900053) / ["안전무지가 2차 사고 불러"](https://www.yna.co.kr/view/AKR20171213165200797) | - 초보 운전자들의 돌발 상황 대처 능력 부족 <br><br> - 커뮤니티(네이버 지식인 등)에 운전 관련 질문이 반복적으로 게시 <br><br> 출처 : [네이버 지식인](https://kin.naver.com/index.nhn?mobile) |

<br>

### 📌 요약 
|🚨문제 상황| 📉영향 | 💡해결책 |
|--------|------|---------|
|운전 도중 검색 불가능|돌발 상황 대처 지연|음성/LLM 기반 실시간 정보 제공|
|초보 운전자의 대처 미숙|2차 사고 치사율이 일반 사고 대비 5배|즉각적인 대응 가이드 제공|
|기존 교육/매뉴얼 효과 한계|사고 상황에서 기억,활용 어려움|상황별 맞춤형 가이드 필요|
|운전 관련 질문 반복|지식 부족 및 불안감 지속|신뢰성 있는 답볍으로 학습 지원|

([운전 중 스마트폰 사용은 음주운전 상태와 유사](https://www.incheonilbo.com/news/articleView.html?idxno=1202536)) 

➡️ LLM 기반 교통 어시스턴트는 운전자들의 당황스러운 각 상황에 즉시 도움을 줄 수 있는 도구로써, 실제적인 안전과 직결 

<br>

## **🔸프로젝트 목표**

### 🛑 **사용자 친화적 교통 어시스턴트 제공**
- 운전자가 음성 또는 텍스트로 질문하면 즉시 이해 가능한 답변을 제시하는 **대화형 인터페이스 제공**

### 🚜 **실시간 안전 대응 지원**
- 교통 사고, 차량 고장, 악천 후 등 돌발 상황 발생 시 **즉각적인 가이드라인을 제공**하여 운전자의 올바른 의사결정 지원

### ⚠️ **운전 지식 상향 평준화**
- 운전자가 본인 상황에 해당하는 공식적인 법률 및 시행령을 쉽게 알아볼 수 있게 하여 운전자들의 운전 지식 상향 평준화를 통해 한ㄱ구의 전반적인 운전사고 감소

---

# 2️⃣ **기술 스택**

| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **LLM** | ![naver-hyperclovax](https://img.shields.io/badge/naver%20hyperclovax-FFB000?style=for-the-badge&logo=naver-hyperclovax&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-005F73?style=for-the-badge&logo=Chainlink&logoColor=white) |
| **벡터 데이터베이스** | ![Chroma](https://img.shields.io/badge/Chroma-009688?style=for-the-badge&logo=Apache&logoColor=white) |
| **임베딩 모델** | ![nlpai-lab/KURE-v1](https://img.shields.io/badge/nlpai%20lab/KURE%20v1-8C9E90?style=for-the-badge&logo=nlpai-lab/KURE-v1&logoColor=white) |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) ![Local](https://img.shields.io/badge/Local-FF4500?style=for-the-badge&logo=Local&logoColor=white) |
| **모델 튜닝/학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![LoRA](https://img.shields.io/badge/LoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **인터페이스(UI)** | ![Streamlit](https://img.shields.io/badge/Streamlit-20B673?style=for-the-badge&logo=Streamlit&logoColor=white) |
| **형상 관리 및 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) |

----

# 3️⃣ **시스템 아키텍처**

## 🔸시스템 아키텍처

<img width="1888" height="1248" alt="image" src="https://github.com/user-attachments/assets/50586735-9ef6-496b-b94b-f85e5a13454e" />



## 🔸 시스템 플로우

**`본 시스템은 사례 데이터 기반 답변 생성과 관련 법규 조항 제시를 통해 운전자에게 실용적이고 근거 있는 안내를 제공하는 AI 아키텍처입니다.`**

### 📋 전체 워크플로우

#### 1️⃣ 사용자 질문 입력
- **입력 방식**: 음성(STT) 또는 텍스트 입력

#### 2️⃣ 데이터 전처리 및 저장
- **사례 데이터**: 실제 운전 사례 및 Q&A → 임베딩 → VectorDB(ChromaDB) 저장
- **법규 데이터**: 교통 법규 문서 → 임베딩 → 별도 VectorDB(ChromaDB) 저장
- **용도 구분**: 사례 데이터(답변 생성용) / 법규 데이터(근거 제시용)

#### 3️⃣ RAG 기반 답변 생성
**Ride Assistance 모드**:
- Retriever가 사용자 질문과 유사한 사례 검색
- sLLM이 검색된 사례를 바탕으로 상황별 맞춤 답변 생성

**Traffic Law Guide 모드**:
- LoRA sLLM이 법규 데이터를 기반으로 법적 해석 제공
- Retriever를 통해 관련 조항 매칭

#### 4️⃣ 통합 응답 출력
- **주요 답변**: 사례 기반 실용적 대응 방법
- **법적 근거**: 관련 교통법규 조항 제시
- **출력 옵션**: 텍스트 응답 + TTS 음성 안내 지원

### 🎯 핵심 특징

✅ **실용성**: 실제 사례 데이터 기반으로 현실적인 답변 제공  
✅ **신뢰성**: 관련 법규 조항을 함께 제시하여 법적 근거 확보  
✅ **편의성**: 음성 입출력 지원으로 주행 중에도 안전한 사용  
✅ **정확성**: 이중 RAG 구조로 답변과 법적 근거의 정합성 보장



---

# 4️⃣ **WBS**

<img width="1453" height="691" alt="image" src="https://github.com/user-attachments/assets/ddec908c-0fe2-418a-809d-e64c4098254e" />


---

# 5️⃣ **요구사항 명세서**

<img width="1293" height="341" alt="image" src="https://github.com/user-attachments/assets/940f5da5-aa5e-46d6-b3be-a6942cf69aa9" />



---

# 6️⃣ **수집한 데이터 및 전처리 요약**


### 🔸가이드 데이터 

| 구분        | 내용 |
|-------------|------|
| **데이터 수집** | 팀원 각각 구축한 질문(Q) - 답변(A) 구조의 텍스트 데이터셋(.json, .jsonl) |
| **데이터 구조** | 질문(`Q`), 답변(`A`) 쌍 |
| **총 데이터 수** | 1,701개 Q&A 레코드 |
| **통합 과정** | JSON과 JSONL 데이터 형식을 모두 읽어 하나의 JSONL(`combined_data.jsonl`)로 병합|
| **전처리 내용** | - JSON 배열 / JSONL 형식 자동 구분<br>- 빈 줄 및 파싱 불가능한 레코드 제거<br>- 필드 구조가 불일치하는 경우 필터링 -> 필드 구조 단일화(`Q`, `A`만 유지) |
| **최종 형식** | JSONL (한 줄당 `{"Q": "...", "A": "..."}` 구조) |

- **데이터 출처** <br>
본 프로젝트에서 활용한 데이터는 교통 안전 관련 Q&A 사례 데이터이며, 
GPT를 활용해 각 예시 상황(Q)에 대한 답변(A)을 출처와 함께 생성한 후, GPT가 생성한 문답이 실제 제도·메뉴얼 및 가이드 등 공개자료와 일치하는지 검증

- **검증 근거 확보** <br>
GPT가 생성한 사례에 대한 답변은 실제 출처 링크를 확인하고 근거 문서와 대조하여 데이터의 신뢰성을 강화

- **데이터 활용 목적** <br>
초보 운전자들이 실제 상황에서 당황하지 않고 대응할 수 있도록, 질문 기반 응급 대처 가이드를 구축

[📄 데이터 출처](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-3rd-5Team/blob/main/data%E1%84%8E%E1%85%AE%E1%86%AF%E1%84%8E%E1%85%A5%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AF)


<br>

### 🔸법령 데이터


<table>
  <tr>
    <th>데이터 출처</th>
    <td>한국도로교통공단 · 도로교통법 외 3개</td>
  </tr>
  <tr>
    <th>데이터 수집</th>
    <td>API Key 활용</td>
  </tr>
  <tr>
    <th>데이터 구조</th>
    <td>
      <img width="392" height="445" alt="데이터 구조 예시"
           src="https://github.com/user-attachments/assets/9c222f50-e068-4eb0-a3e1-6875b6556689" />
    </td>
  </tr>
  <tr>
    <th>총 데이터 수</th>
    <td>조문-항 단위로 통합 시<br><b>1,434개</b></td>
  </tr>
  <tr>
    <th>전처리 내용</th>
    <td>
      1. <b>구조 단위 저장</b><br>
      - 기본 단위: 조–항–호<br>
      - 단, 호 단위만 단독 저장 시 문맥 단절 발생 → 각 항에 포함된 모든 호를 병합 저장 (“항내용 + 호내용…”)<br><br>
      2. <b>불필요 조항 제거 (패턴 필터링)</b><br>
      - 특정 키워드만 포함된 문구(예: <code>제\d+항에 따른</code>, <code>제\d+조에 따른</code>)는 실질적 내용이 없어 제거<br><br>
      3. <b>주제 외 내용 제거</b><br>
      - 교통 어시스턴트 목적과 직접 관련 없는 조항 제외<br>
      - 제거 키워드 예시:<br>
      &nbsp;&nbsp;• 정의 (법률 개념 정의 전반)<br>
      &nbsp;&nbsp;• 학원, 수강 (운전면허 학원 외 일반 교육 관련)<br>
      &nbsp;&nbsp;• 행정 절차, 기관 운영, 개인정보 처리 등
    </td>
  </tr>
  <tr>
    <th>최종 형식</th>
    <td>
            <pre>{"id": "...법_제n조...","content": "...","metadata": {"source_type": "law","article_title": "..."}}</pre>
    </td>
  </tr>
</table>

---

# 7️⃣ **DB 연동 구현 코드**

- [**DB 연동 구현 코드 파일**](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-3rd-5Team/blob/main/build_vectordb.py)
- **[📁임베딩 모델 (github)](https://github.com/nlpai-lab/KURE?tab=readme-ov-file)**
- 벡터 DB: ```Chroma```

### ✅ DB 구축 과정 상세 요약
- **데이터 변환** : ```jsonl``` 형식의 질의응답 데이터를 ```Langchain```의 ```Document``` 객체로 변환
- **자동 청킹** : ```RecursiveCharacterTextSplitter```를 사용해 문서 분할
- **벡터화** : 한국어 특화 임베딩 모델인 ```nlpai-lab/KURE-v1```을 사용해 ```Document```를 고차원 벡터로 변환
- **DB 저장** : 대규모의 데이터가 아니기 때문에 벡터화된 데이터를 ```Chroma``` Vector DB에 저장하여 RAG 시스템에서 활용할 수 있도록 준비


---

# 8️⃣ **LLM 모델 선정 이유**
### 🤖가이드 - 사용된 LLM 모델 : ```naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B```

### 🔸모델 선택 이유
1. **✅성능과 효율성의 균형**
     - 1.5B라는 비교적 작은 파라미터 크기는 **빠른 추론 속도**를 보장 > 운전 중 긴급 질문에 실시간으로 응답해야 하는 A.D.A 서비스에 필수적 요건

<br>

2. **✅한국어 특화 성능**
    - 네이버가 개발한 **한국어 특화 모델**로써, 구어체 질문이나 운전 전문 용어에 대한 이해도 높음
    
<br>

3. **✅On-device 구동 가능성 및 확장성**
    - 모델 경량성은 클라우드 환경에서 운영 비용을 절감할 뿐만 아니라 네트워크 연결 없이도 작동하는 **On-Device AI**로의 확장 가능성
  
<br>
  
### ⚜️법적 근거 - 사용된 LLM 모델 : ```naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B``` 

### 🔸모델 선택 이유
  
  **✅파라미터 확대**
  - 법령의 경우, 복잡하고 중의적인 문장 구조를 해석하고 법률 용어의 미묘한 의미 차이를 정확히 이해하는 능력 필수
  - 3B 모델은 1.5B 모델보다 더 많은 파라미터를 보유하여 이러한 고도의 언어적 복잡성 처리에 유리
  - 응답이 정확성과 신뢰도가 중요하기 때문에 법적 근거와 같은 민감한 정보를 다루는 데 더 적합

---

# 9️⃣ **테스트 계획 및 결과 보고서**

[**🗂️테스트 계획 및 결과 보고서**](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-3rd-5Team/blob/main/SKN17-3rd-5Team_%ED%85%8C%EC%8A%A4%ED%8A%B8_%EA%B3%84%ED%9A%8D_%EB%B0%8F_%EA%B2%B0%EA%B3%BC_%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)

### 🔸평가 방식
- 총 10개 질문(일상 주행, 돌발 상황, 법규/상식), 5개의 항목, 5점 만점 정성 평가로 진행 


### 🔸평가 기준 항목
<img width="742" height="310" alt="image" src="https://github.com/user-attachments/assets/e2bee7c3-f7ee-4a71-89c6-7faf295c12d4" />



### 🔸테스트 결과
|평가 항목|분석 및 비고|
|--------|-------------|
|응답 속도|5초 이내의 빠른 답변|
|답변 완결성|일반적인 상황에 대해 답변 완결|
|답변 일관성|같은 질문에도 구조, 논리 유지|
|모델 안정성|질문 다양성에도 구조 안정적으로 유지| 
|의도 파악 정확성|제공된 답변이 사실과 일치|


### 🔸테스트 결론
- 빠른 응답 속도
  - 사용자의 다양한 질문에 대해 전반적으로 빠르고 정확한 답변을 제공하는 것으로 평가
 
- 답변 품질 보통
  - 운전자의 안전을 최우선으로 고려하는 답변
  - On-Device에서의 구동 가능이라는 목표 달성
  - 운전자가 직면할 수 있는 보편적인 돌발 상황 같은 경우에는 응답 품질이 좋지만, 더 디테일하고 복잡한 상황에서는 성능이 떨어지는 응답 품질 확인 
 
- 근거 제시
  - 법적이나 매뉴얼 출처를 분명히 해 신뢰성 있는 답변 제시

- 응답 형식 일관성
  - ```문제가 되는 이유``` > ```행동 가이드``` 순으로 1, 2, 3, 4번으로 단계형 답변 구조 유지 


---

# 🔟 **진행 과정 중 프로젝트 개선 노력**

### 🔸개선 전 문제점
- Vector DB에서 질문과 관련성이 낮은 문서를 검색
- LLM이 검색된 정보를 활용하지 못하고 단답형으로 답변 
- 매 질문을 독립적인 것으로 인식하여 "그래서?" 와 같은 후속 질문을 이해하지 못함
- 프롬프트 메세지가 응답에 그대로 출력됨

### 🔸개선 노력

#### 1. 프롬프트 엔지니어링
- 고품질의 답변을 위해 프롬프트를 길고 명확하게 작성할수록 오히려 답변의 품질이 떨어지는 현상 <br>
- 오히려 간략하지만 명확한 프롬프트로 LLM이 일관성 있고 전문적인 페르소나를 유지하며 답변을 더 가공하여 제공하도록 프롬프트 엔지니어링 

#### 2. Q 데이터 셋
- Q-A 데이터 세트 전체를 context로 넘겨주어 관련성이 낮은 문서를 retriever가 탐색하는 문제를 page_content에는 질문만 담고 metadata에 답변을 담아 사용자의 질의에 가장 부합하는 문서를 검색할 수 있도록 개선 

#### 3. 메모리 기능 추가 
- 후속 질문이나 대명사를 이해하지 못해 대화 단절 문제 <br>
- 이전 대화도 기억해내기 위해 메모리 기능 추가 시도


---

# 📜 **수행 결과**

<img width="1778" height="944" alt="image" src="https://github.com/user-attachments/assets/a59c5c9f-275d-4245-af98-fb19faeafb0f" /> <br>
<img width="1801" height="957" alt="image" src="https://github.com/user-attachments/assets/4992fc19-12b9-438e-a34e-fdbfff14ad0e" />
<img width="1237" height="416" alt="image" src="https://github.com/user-attachments/assets/54c913e8-4728-416e-a4b6-61fff248fff5" />




---

# 📒 **결과 정리 및 향후 계획**

### 🔸프로젝트 결과 요약
운전 중 발생하는 다양한 돌발 상황에 대해 실시간으로 대처 방안을 제공하는 LLM 기반의 질의 응답 시스템인 **A.D.A(AI Driving Assistant)** 를 성공적으로 개발

- RAG 기반의 신뢰성 높은 답변 생성
- 프롬프트 엔지니어링과 대화 메모리 기능 추가로 사용자 친화적인 대화 인터페이스 구축
- 실제 법령 데이터를 근거로 답변 기능  


### 🔸기대 효과

- **2차 사고 예방** : 사고 발생 시 당황하지 않고 신속하고 정확한 초기 대응을 하도록 유도하여 2차 사고 발생률을 낮추는 데 기여
- **정보 접근성 향상** : 기존의 두꺼운 차량 매뉴얼이나 인터넷 검색의 번거로움을 해소하고 직관적인 인터페이스로 누구나 쉽게 필요한 정보에 접근 가능 


### 🔸향후 개선 방향
- **핸즈프리** : STT + TTS 기술을 접목해 운전자가 주행 중에 음성으로 질문하고 음성으로 답변하는 기술 탑재
- **응답 생성 시간 단축** : 실시간으로 상담 하기 위한 처리 경량화 및 속도 개선
- **사용자 질문 라우팅 시도** : 사용자와의 이전 대화를 기억해 맥락에 맞는 답변 제공 


----

# **한 줄 회고**

|이름|회고록|
|--------|--------|
|**임길진**| 법령이라는 특수한 데이터셋에서 전처리하는 과정과 벡터 DB 에서 검색이 잘 되도록 조정하는 과정이 보람찼습니다.  |
|**박민정**| 신뢰성이 중요한 RAG 데이터셋을 만드는 과정이 매우 힘들었지만 정제하고 아키텍처를 구축해 나가는 과정이 뿌듯했습니다. |
|**이가은**| 사전 계획과 아키텍처가 기술적·시간적 한계에 부딪히며 여러 문제들을 겪었지만, 이를 해결하며 RAG 파이프라인을 완성해 나간 과정이 보람찼습니다. |
|**한 훈**| 데이터 수집부터 시작하여 프로젝트가 진행될 수록 사전에 수립한 아키텍쳐나 계획이 기술적/시간적 한계에 봉착하여 그것을 타파히기 위해 노력한 과정이 고통스러웠으면서도 뿌듯했습니다. |




