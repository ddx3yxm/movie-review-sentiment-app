# 🎬 AI 영화 리뷰 감성 분석 & 데이터 대시보드

> **Streamlit**을 활용하여 데이터 시각화 차트와 키워드 기반 감성 분석 로직을 웹 서비스 형태로 구현한 토이 프로젝트입니다.

[👉 웹 실행하기](https://movie-review-sentiment-app-6cbad39by4ayereq8qky5r.streamlit.app/)

---

## 📌 주요 기능

* **장르별 평점 대시보드:** 영화 장르별 평균 평점과 총 리뷰 수를 요약 지표 및 바 차트로 시각화
* **리뷰 감성 분석 AI:** 사용자 리뷰 텍스트 입력 시 키워드 사전 기반 감성을 파악하여 긍정/부정/중립 여부 실시간 예측

---

## 🛠️ 기술 스택

| 분류 | 사용 기술 |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Library** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) |
| **Web Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| **Deployment** | ![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |

---

## 📁 프로젝트 구조

```text
├── app.py
├── requirements.txt
└── README.md   
```

---

## 프로젝트를 통해 배운 점

### 1. 웹 서비스 배포 파이프라인 경험
* 단순 분석 코드 작성에 그치지 않고, Streamlit Cloud를 활용해 가벼운 파이썬 코드만으로 실시간 접근 가능한 웹 애플리케이션을 구현하고 배포하는 전 과정을 경험했다.

### 2. 사용자 중심의 UI/UX 및 예외 처리 고려
* 사용자가 빈 값을 입력하거나 잘못된 텍스트를 제출했을 때 오류가 발생하지 않도록 예외 처리 조건문을 작성하였고, 분석 결과를 시각적으로 직관적이게 보여주기 위해 경고창 및 성공 결과 카드 UI를 구현했다.

### 3. 한계점 및 향후 발전 방향
* **한계점:** 현재 로직은 정해진 키워드 유무를 판별하는 기초적 방식이므로, 뉘앙스나 맥락을 완벽히 읽어내지 못하는 한계가 있다.
* **발전 방향:** 추후에는 사전 학습된 한국어 NLP 모델을 접목하여 분석 정확도를 한 단계 높여볼 계획 !
