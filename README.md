# SKN 17기 - 3rd Project 5Team 
> **주제** : LLM을 연동한 내외무 문서 기반 질의 응답 시스템  
  개발 기간: 2025.09.24 ~ 2025.09.25

---

# 🔖 목차 

<details>
<summary>목차 내용</summary>

### 1. [팀 소개](#0️⃣-팀-소개)  
### 2. [프로젝트 개요](#1️⃣-프로젝트-개요)  
### 3. [기술 스택](#2️⃣-기술-스택)  
### 4. [시스템 아키텍처](#3️⃣-시스템-아키텍쳐)  
### 5. [WBS](#4️⃣-wbs)  
### 6. [요구사항 명세서](#5️⃣-요구사항-명세서)  
### 7. [수집한 데이터 및 전처리 요약](#6️⃣-수집한-데이터-및-전처리-요약)  
### 8. [DB 연동 구현 코드](#7️⃣-db-연동-구현-코드)  
### 9. [모델 선정 이유](#8️⃣-모델-선정-이유)  
### 10. [테스트 계획 및 결과 보고서](#9️⃣-테스트-계획-및-결과-보고서)  
### 11. [진행 과정 중 프로젝트 개선 노력](#🔟-진행-과정-중-프로젝트-개선-노력)  
### 12. [수행 결과](#*️⃣-수행-결과)  
### 13. [한 줄 회고](#✳️-한-줄-회고)  

</details>

---

# 0️⃣ **팀 소개**
## **팀명: 모빌리티 브레인**
- 교통 관련한 두뇌를 맡는다는 의미

## **팀원 소개** (사진 각자 아바타 만들어오기)
| [@임길진](https://github.com/LGJ0405)                      | [@박민정](https://github.com/minjeon)                       |  [@이가은](https://github.com/Leegaeune)                       | [@한 훈](https://github.com/Hoonieboogie)                       |
|---------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| <img src="https://github.com/user-attachments/assets/e7dd2863-b577-4385-a46c-7163efb0bfe4" width="200" height="200">         | <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/f58448d7-9ece-412a-bb50-5c963a6af3df" />| <img src="https://github.com/user-attachments/assets/c80b5b8d-4a42-4ed1-950f-b0ea5b078f51" width="200" height="200">             |  <img src="https://github.com/user-attachments/assets/7fdacbe3-b568-4c42-8758-d189ec522bc3" width="200" height="200" />|



---

# 1️⃣ **프로젝트 개요**
## **프로젝트 명: 교통 어시스턴트**
## **🚗프로젝트 소개**

**교통 어시스턴트**는 운전자들이 도로 위에서 겪을 수 있는 모든 돌발 상황에 대해 대처법과 가이드를 실시간으로 제공하는 챗봇입니다. 

## **프로젝트 필요성**

| <img width="800" height="325" alt="image" src="https://github.com/user-attachments/assets/3441bff3-793f-4bc8-bfb5-d0362f8d3803" /> | <img width="822" height="500" alt="image" src="https://github.com/user-attachments/assets/e47ecf3f-6de8-41f2-bf94-b4bd96bf78ff" />|
|---------------------------|---------------------------|
| - 자동차 고장·사고 시 당황으로 인한 2차 사고 위험 <br><br> - 교통 사고 2차 사고 치사율 54% - "고속도로 한복판에서 시동 꺼진 차량, 운전자가 대처 방법 몰라 뒤따라오던 차량과 추돌" 같은 경우 자주 보도 <br><br> 출처 : https://www.yna.co.kr/view/AKR20240319052900053  | - 초보 운전자들의 돌발 상황 대처 X <br><br> - 커뮤니티(네이버 지식인 등)에 운전 관련 질문이 반복적으로 게시 <br><br> 출처 : https://kin.naver.com/index.nhn?mobile |

📌 요약
<br>
- 운전 도중 검색은 불가능 (불법)
- 기존 교통 교육/매뉴얼은 사전에 읽지 않으면 쓸모 X
- 돌발 상황에서 당황 + 지식 부족으로 대처 X
<br>
➡️ LLM 기반 교통 어시스턴트는 운전자들의 당황스러운 각 상황에 즉시 도움을 줄 수 있는 도구로써, 실제적인 안전과 직결

## **프로젝트 목표**

### 🛑 **사용자 친화적 교통 어시스턴트 제공**
- 운전자가 음성 또는 텍스트로 질문하면 즉시 이해 가능한 답변을 제시하는 **대화형 인터페이스 제공**

### 🚜 **실시간 안전 대응 지원**
- 교통 사고, 차량 고장, 악천 후 등 돌발 상황 발생 시 **즉각적인 가이드라인을 제공**하여 운전자의 올바른 의사결정 지원

---

# 2️⃣ **기술 스택**

| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **LLM** | ![OpenChat](https://img.shields.io/badge/OpenChat-FFB000?style=for-the-badge&logo=OpenAI&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-005F73?style=for-the-badge&logo=Chainlink&logoColor=white) |
| **벡터 데이터베이스** | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge&logo=Apache&logoColor=white) |
| **임베딩 모델** | ![OpenAI Embeddings](https://img.shields.io/badge/OpenAI%20Embeddings-8C9E90?style=for-the-badge&logo=OpenAI&logoColor=white) |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) |
| **모델 튜닝/학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![LoRA](https://img.shields.io/badge/LoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **인터페이스(UI)** | ![Gradio](https://img.shields.io/badge/Gradio-20B673?style=for-the-badge&logo=Gradio&logoColor=white) |
| **형상 관리 및 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) ![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=Google%20Drive&logoColor=white) |

----

# 3️⃣ **시스템 아키텍처**

## 🔸시스템 아키텍처



## 🔸시스템 플로우


---

# 4️⃣ **WBS**




---

# 5️⃣ **요구사항 명세서**


---

# 6️⃣ **수집한 데이터 및 전처리 요약**
- 출처
- 수집 방식
- 전처리 과정
- 최종 데이터양
- 데이터 구조
- 최종 데이터 프레임

// 
문서 구성 및 벡터화 > 이게 RAG인가?

// 
RAG


| 구분        | 내용 |
|-------------|------|
| **데이터 수집** | 팀원 각각 구축한 질문(Q) - 답변(A) 구조의 텍스트 데이터셋(.json, .jsonl) |
| **데이터 구조** | 질문(`Q`), 답변(`A`) 쌍 |
| **총 데이터 수** | 1,701개 Q&A 레코드 |
| **통합 과정** | JSON과 JSONL 데이터 형식을 모두 읽어 하나의 JSONL(`combined_data.jsonl`)로 병합|
| **전처리 내용** | - JSON 배열 / JSONL 형식 자동 구분<br>- 빈 줄 및 파싱 불가능한 레코드 제거<br>- 필드 구조가 불일치하는 경우 필터링 -> 필드 구조 단일화(`Q`, `A`만 유지) |
| **최종 형식** | JSONL (한 줄당 `{"Q": "...", "A": "..."}` 구조) |



---

# 7️⃣ **DB 연동 구현 코드**



---

# 8️⃣ **모델 선정 이유**
- 사용된 LLM
- 모델 선정 기준
- 이 모델을 선택한 이유 요약약


---

# 9️⃣ **테스트 계획 및 결과 보고서**
- 평가 방식
  어떤 식으로 평가를 했는지
- 테스트 결과
- 테스트 결론 


---

# 🔟 **진행 과정 중 프로젝트 개선 노력**
- 진행 중 어떠한 문제점이 있었음
- 해결하기 위한 방식들 과 그에 해당하는 결과 



---

# 📜 **수행 결과**
- streamlit 구현 페이지 (아님 다른거)



---

# 🍀 **결과 정리 및 향후 개선 방향**
- 프로젝트 결과 요약
- 기대 효과
- 향후 개선 방향 





----

# **한 줄 회고**

