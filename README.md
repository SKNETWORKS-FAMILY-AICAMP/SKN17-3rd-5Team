# SKN 17기 - 3rd Project 5Team 
> **주제** : LLM을 연동한 내외무 문서 기반 질의 응답 시스템  
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

**A.D.A**는 운전자들이 주행 중 맞닥뜨릴 수 있는 다양한 돌발 상황에 대해 실시간으로 대처법, 가이드, 안전 수칙을 제공하는 LLM 기반 챗봇입니다. 음성이나 텍스트로 질문하면 즉시 답변을 제공하여 운전자 스스로 빠르고 정확하게 대응할 수 있도록 돕습니다. 

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

---

# 2️⃣ **기술 스택**

| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **LLM** | ![naver-hyperclovax](https://img.shields.io/badge/naver%20hyperclovax-FFB000?style=for-the-badge&logo=naver-hyperclovax&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-005F73?style=for-the-badge&logo=Chainlink&logoColor=white) |
| **벡터 데이터베이스** | ![Chroma](https://img.shields.io/badge/Chroma-009688?style=for-the-badge&logo=Apache&logoColor=white) |
| **임베딩 모델** | ![nlpai-lab/KURE-v1](https://img.shields.io/badge/nlpai%20lab/KURE%20v1-8C9E90?style=for-the-badge&logo=nlpai-lab/KURE-v1&logoColor=white) |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) |
| **모델 튜닝/학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![LoRA](https://img.shields.io/badge/LoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **인터페이스(UI)** | ![Streamlit](https://img.shields.io/badge/Streamlit-20B673?style=for-the-badge&logo=Streamlit&logoColor=white) |
| **형상 관리 및 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) |

----

# 3️⃣ **시스템 아키텍처**

## 🔸시스템 아키텍처

<img width="2030" height="1284" alt="image" src="https://github.com/user-attachments/assets/5dd8baff-07c8-47a6-b6c3-824c74b2cfc9" />




## 🔸시스템 플로우

본 시스템은 사용자의 질문에 대해 **사례 데이터 기반으로 답변을 생성**하고,  
필요시 그 답변에 연관된 **법규 조항을 함께 제시**하는 AI 아키텍처입니다.


1) 사용자 질문 입력
- 운전 중 상황 또는 교통 관련 궁금증을 음성(STT) 또는 텍스트로 입력  
- 모드 선택:  
  - 🚗 **Ride Assistance** – 실시간 주행 상황 대응  
  - ⚖️ **Traffic Law Guide** – 법규 해설 및 관련 조항 제시


2) 사례 및 법규 데이터 전처리
- 실제 운전 사례 및 상황별 Q&A 데이터를 수집하여 임베딩  
- 교통 법규 문서를 별도로 벡터화하여 **VectorDB (ChromaDB)** 에 저장  
- 두 데이터는 각각 **답변 생성용(사례)** / **근거 제시용(법규)** 으로 활용



3) 사례 기반 답변 생성 (RAG)
- **Retriever**가 사용자 질문과 유사한 사례를 검색  
- **sLLM**이 사례를 참고하여 사용자 상황에 맞는 답변 생성


4) 관련 법규 조항 제시
- 생성된 답변과 연결되는 법규를 **VectorDB**에서 추가 검색  
- 답변 하단 또는 별도 섹션에 **관련 조항을 자동으로 제시**


5) 응답 출력
- **상황별 대응 방법**과  
- **관련 법규 조항(예: 도로교통법 제XX조)** 를 함께 제공  
- 필요 시 **TTS 모델**을 통해 음성 안내도 지원


💡 **핵심 특징**
- 답변은 **사례 데이터 기반**으로 생성되어 실제 상황 대응에 적합  
- **관련 법규 조항을 제시**하여 법적 근거 확인 가능  



---

# 4️⃣ **WBS**

<img width="1425" height="660" alt="image" src="https://github.com/user-attachments/assets/c2f2f9eb-3400-4687-b279-05f9e5dd4da1" />

---

# 5️⃣ **요구사항 명세서**

<img width="1550" height="400" alt="image" src="https://github.com/user-attachments/assets/0f886b44-3392-4a06-9f70-99199b8d4ade" />


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

- DB 연동 구현 코드 파일 하이퍼링크 달기 
- **[📁임베딩 모델 (github)](https://github.com/nlpai-lab/KURE?tab=readme-ov-file)**
- 벡터 DB: ```Chroma```

### ✅ DB 구축 과정 상세 요약
- **데이터 변환** : ```jsonl``` 형식의 질의응답 데이터를 ```Langchain```의 ```Document``` 객체로 변환
- **자동 청킹** : ```RecursiveCharacterTextSplitter```를 사용해 문서 분할
- **벡터화** : 한국어 특화 임베딩 모델인 ```nlpai-lab/KURE-v1```을 사용해 ```Document```를 고차원 벡터로 변환
- **DB 저장** : 벡터화된 데이터를 ```Chroma``` Vector DB에 저장하여 RAG 시스템에서 활용할 수 있도록 준비


---

# 8️⃣ **LLM 모델 선정 이유**
### 🔸사용된 LLM 모델 : ```naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B```

### 🔸모델 선택 이유
1. **✅성능과 효율성의 균형**
     - 1.5B라는 비교적 작은 파라미터 크기는 **빠른 추론 속도**를 보장 > 운전 중 긴급 질문에 실시간으로 응답해야 하는 A.D.A 서비스에 필수적 요건

<br>

2. **✅한국어 특화 성능**
    - 네이버가 개발한 **한국어 특화 모델**로써, 구어체 질문이나 운전 전문 용어에 대한 이해도 높음
    
<br>

3. **✅On-device 구동 가능성 및 확장성**
    - 모델 경량성은 클라우드 환경에서 운영 비용을 절감할 뿐만 아니라 네트워크 연결 없이도 작동하는 **On-Device AI**로의 확장 가능성 

---

# 9️⃣ **테스트 계획 및 결과 보고서**

평가 항목
- 정확성 : 답변이 사실에 근거하는가? DB에서 검색된 정보를 충실히 반영하는가?
- 견고성 : 사소한 오류에도 질문 의도를 파악하는가? 서비스 범위를 벗어난 질문에 대해 적절히 거절하는가?
- 응답 속도 : 5초 이내로 답변이 생성되는가?
- 사용성 : 기능 사용법이 명확한가? 대화 흐름이 자연스러운가?

|평가 항목|결과|분석 및 비고|
|--------|----|-------------|
|정확성| % |DB에 없는 질문이나 매우 지엽적인 질문에 대해서는 다소 일반적인 답변을 생성하는 경향을 보임|
|견고성| 양호 | 오타나 간단한 비문을 잘 처리했으나 서비스 범위를 벗어난 질문에 대해서는 명확히 답변하지 못함|
|응답 속도|평균 몇 초|RunPod 환경에서 목표했던 5초 이내의 응답 속도 만족|
|사용성|긍정적|UI가 직관적이고 사용이 편리하다는 공통된 의견, 대화 기록이 남아 이전 질문을 참고하기 좋다는 피드백|

---

# 🔟 **진행 과정 중 프로젝트 개선 노력**

### 🔸개선 전 문제점
- Vector DB에서 질문과 관련성이 낮은 문서를 검색
- LLM이 검색된 정보를 활용하지 못하고 단답형으로 답변 
- 매 질문을 독립적인 것으로 인식하여 "그래서?" 와 같은 후속 질문을 이해하지 못함
- 프롬프트 메세지가 응답에 그대로 출력됨

#### 1. 프롬프트 엔지니어링
LLM이 DB에서 검색된 정보를 그대로 나열하거나 질문의 핵심을 벗어난 일반적인 답변 생성 문제 <br>
프롬프트 템플릿에 역할 부여, 답변 형식 지정, 어조 설정 등 구체적인 지침 추가로 LLM이 일관성 있고 전문적인 페르소나를 유지하며 답변을 더 가공하여 제공하도록 프롬프트 엔지니어링 

#### 2. 메모리 기능 추가 
후속 질문이나 대명사를 이해하지 못해 대화 단절 문제 <br>
이전 대화도 기억해내기 위해 메모리

#### 3. Chunking 전략 수정
초기에는 문서를 고정된 크기로 분할 > 정보의 의미 단위가 깨지는 문제 발생 <br>
```RecursiveCharacterTextSplitter```를 사용하여 문단의 의미가 최대한 유지되도록 청크를 분할하고 청크 간의 중첩 영역을 설정하여 문맥이 끊어지지 않도록 개선

---

# 📜 **수행 결과**

실행 페이지 화면


---

# 📒 **결과 정리 및 향후 계획**

### 🔸프로젝트 결과 요약
운전 중 발생하는 다양한 돌발 상황에 대해 실시간으로 대처 방안을 제공하는 LLM 기반의 질의 응답 시스템인 **A.D.A**를 성공적으로 개발

- RAG 기반의 신뢰성 높은 답변 생성
- 프롬프트 엔지니어링과 대화 메모리 기능 추가로 사용자 친화적인 대화 인터페이스 구축
- 실제 법령 데이터를 근거로 답변 기능  


### 🔸기대 효과

- **2차 사고 예방** : 사고 발생 시 당황하지 않고 신속하고 정확한 초기 대응을 하도록 유도하여 2차 사고 발생률을 낮추는 데 기여
- **정보 접근성 향상** : 기존의 두꺼운 차량 매뉴얼이나 인터넷 검색의 번거로움을 해소하고 직관적인 인터페이스로 누구나 쉽게 필요한 정보에 접근 가능 


### 🔸향후 개선 방향
- **핸즈프리** : STT + TTS 기술을 접목해 운전자가 주행 중에 음성으로 질문하고 음성으로 답변하는 기술 탑재
- **응답 생성 시간 단축** : 실시간으로 상담 하기 위한 처리 경량화 및 속도 개선
- **사용자 질문 라우팅 시도** : ??
- **멀티모달 기능 추가** : 계기판의 경고등 사진 등을 찍어 전송하면 이미지를 분석해 어떤 문제인지 알려주고 해결책을 제시하는 비전 기능 추가 가능


----

# **한 줄 회고**

|이름|회고록|
|--------|--------|
|**임길진**| 왜 |
|**박민정**| 힘들다... 힘들어요.. |
|**이가은**| 되 |
|**한 훈**| 냐 |
