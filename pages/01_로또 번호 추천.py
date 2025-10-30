import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="🍪🎂 로또 번호 추첨기", page_icon="🎂")

# 배경 꾸미기용 스타일 (이모티콘, 색상)
st.markdown(
    """
    <style>
    body {
        background-color: #fff7f0; /* 따뜻한 크림색 배경 */
    }
    .title {
        text-align: center;
        font-size: 2.2em;
        color: #ff7b7b;
    }
    .result {
        background-color: #fff0f5;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown("<h1 class='title'>🍪🎂 달콤한 로또 추첨기 🎂🍪</h1>", unsafe_allow_html=True)

st.write("쿠키 굽듯이 번호를 구워볼까요? 🍰 1~45 사이 숫자 중 6개를 랜덤으로 추첨합니다!")

# ✅ 게임 수 직접 입력
num_sets = st.number_input("🍪 몇 게임을 추첨할까요?", min_value=1, max_value=100, value=5, step=1)

# ✅ 추첨 버튼
if st.button("🎂 번호 굽기 시작 🎰"):
    st.subheader("🍪 추첨 결과 🍪")
    for i in range(num_sets):
        numbers = sorted(random.sample(range(1, 46), 6))
        st.markdown(
            f"<div class='result'>🎂 **게임 {i+1}:** "
            + " 🍪 ".join([f"`{n}`" for n in numbers]) +
            "</div>",
            unsafe_allow_html=True
        )

st.markdown("---")
st.caption("💡 각 게임은 중복 없이 1~45 사이의 6개 번호를 랜덤으로 추첨합니다. 🍰")
