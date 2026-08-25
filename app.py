import pandas as pd
import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="영화 리뷰 감성 분석 & 대시보드", page_icon="🎬", layout="centered"
)

# 2. 헤더 타이틀
st.title("🎬 AI 영화 리뷰 감성 분석기")
st.write(
    "데이터 시각화와 키워드 기반 감성 분석을 제공하는 Streamlit 토이 프로젝트입니다."
)
st.markdown("---")

# 3. 탭 구성
tab1, tab2 = st.tabs(["📊 장르별 평점 대시보드", "🔮 리뷰 감성 분석 AI"])

# --- TAB 1: 데이터 대시보드 ---
with tab1:
    st.subheader("장르별 영화 평균 평점 및 리뷰 수")

    # 가상 데이터 생성
    data = pd.DataFrame(
        {
            "장르": ["SF/메카닉", "액션/스릴러", "드라마", "코미디", "공포"],
            "평균 평점 (10점 만점)": [8.9, 8.4, 9.1, 7.8, 7.2],
            "총 리뷰 수": [2400, 1850, 3100, 1200, 950],
        }
    )

    # 요약 지표 (Metrics)
    col1, col2 = st.columns(2)
    col1.metric("최고 평점 장르", "드라마 (9.1점)")
    col2.metric("최다 리뷰 장르", "드라마 (3,100개)")

    st.write("")
    # 표 출력
    st.dataframe(data, use_container_width=True)

    # 바 차트 시각화
    st.subheader("장르별 평균 평점 비교")
    st.bar_chart(data.set_index("장르")["평균 평점 (10점 만점)"])

# --- TAB 2: 리뷰 감성 분석 ---
with tab2:
    st.subheader("영화 리뷰 긍정/부정 예측")
    st.write("리뷰를 입력하면 AI 분석 로직이 감정을 파악합니다.")

    # 사용자 리뷰 입력
    user_review = st.text_area(
        "리뷰 내용을 입력하세요:",
        value="이 영화 연출이랑 몰입감이 대박이네요! 올해 본 영화 중 최고입니다.",
        height=100,
    )

    if st.button("감성 분석 실행", type="primary"):
        if not user_review.strip():
            st.warning("리뷰를 입력해 주세요!")
        else:
            # 키워드 사전
            pos_words = [
                "대박",
                "최고",
                "추천",
                "명작",
                "감동",
                "재밌",
                "몰입감",
                "인생작",
                "좋",
            ]
            neg_words = [
                "최악",
                "노잼",
                "지루",
                "아쉽",
                "실망",
                "별로",
                "돈아깝",
                "망",
            ]

            pos_count = sum(word in user_review for word in pos_words)
            neg_count = sum(word in user_review for word in neg_words)

            st.markdown("---")
            st.markdown("### 분석 결과")

            if pos_count > neg_count:
                st.success("**[긍정 리뷰]**로 분석되었습니다!")
                st.balloons()
            elif neg_count > pos_count:
                st.error("**[부정 리뷰]**로 분석되었습니다.")
            else:
                st.info("**[중립 또는 분류 중립]** 리뷰입니다.")
