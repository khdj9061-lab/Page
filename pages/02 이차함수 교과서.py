import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 제목 ---
st.title("📘 이차함수 교과서")
st.write("**이차함수의 개형을 함께 탐구해봅시다!**")

# --- 배경색 설정 ---
st.sidebar.header("배경 설정 🎨")
bg_color = st.sidebar.color_picker("교과서 배경색을 선택하세요:", "#F5F5DC")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 슬라이더로 a값 조정 ---
st.header("1️⃣ 이차함수 y = a x² 의 그래프 개형 탐구")
a = st.slider("a 값을 조정해보세요:", -5.0, 5.0, 1.0, 0.1)

# --- 그래프 그리기 ---
x = np.linspace(-5, 5, 200)
y = a * x**2

fig, ax = plt.subplots()
ax.plot(x, y, color="royalblue", linewidth=2)
ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = {a}x²")
st.pyplot(fig)

# --- 성질 설명 ---
st.subheader("그래프의 성질 🧠")

if a > 0:
    st.success("a > 0 이므로 그래프는 **아래로 볼록(위에 열린 U자 모양)** 입니다.")
elif a < 0:
    st.warning("a < 0 이므로 그래프는 **위로 볼록(아래에 열린 U자 모양)** 입니다.")
else:
    st.info("a = 0 이므로 y = 0, 즉 x축 위의 직선이 됩니다.")

# --- 개념 확인 문제 ---
st.header("2️⃣ 개념 확인 문제 ✏️")
st.write("**문제:** 이차함수 y = a x² 에서 a < 0 일 때, 그래프는 어떤 모양인가요?")
st.write("① 아래로 볼록  ② 위로 볼록")

answer = st.text_input("정답 번호를 입력하세요 (예: ① 또는 1):")

if answer:
    if answer.strip() in ["②", "2"]:
        st.success("🎉 참 잘했어요!")
    else:
        st.error("다시 시도해보아요^^")

st.write("---")
st.caption("© 2025 수학 교과서 제작 프로젝트 – Streamlit으로 만든 디지털 교재 예시")
