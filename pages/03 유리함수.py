import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="Rational Function y = k/(x - p) + q", layout="centered")

# 💠 배경색 설정
page_bg_color = """
<style>
.stApp {
    background-color: #d4f4ff;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# 제목
st.title("💡 Rational Function Visualization: y = k / (x - p) + q")

# 개념 설명
st.markdown("""
A **rational function** of this form is expressed as:

### 👉  y = k / (x - p) + q

- **k** : Controls the shape and direction (reflection) of the graph  
- **p** : Determines the **vertical asymptote** (x = p)  
- **q** : Determines the **horizontal asymptote** (y = q)  

The function is undefined when x = p,  
and the graph consists of two separate branches.
""")

# 🎛️ 슬라이더 설정
st.sidebar.header("⚙️ Adjust Coefficients")
k = st.sidebar.slider("k (numerator coefficient)", -10.0, 10.0, 1.0, step=0.1)
p = st.sidebar.slider("p (vertical asymptote position)", -50.0, 50.0, 0.0, step=0.5)
q = st.sidebar.slider("q (horizontal asymptote position)", -50.0, 50.0, 0.0, step=0.5)

# x 값 설정
x = np.linspace(-100, 100, 2000)

# 분모가 0이 되는 점 제외
mask = (x - p) != 0
y = np.zeros_like(x)
y[mask] = k / (x[mask] - p) + q

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x[mask], y[mask], color='blue', label="y = k / (x - p) + q")

# 점근선 표시 (영문으로 변경)
ax.plot([p, p], [-100, 100], color='red', linestyle='--', label=f"Vertical Asymptote: x = {p:.2f}")
ax.plot([-100, 100], [q, q], color='green', linestyle='--', label=f"Horizontal Asymptote: y = {q:.2f}")

# 기준선
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# 그래프 꾸미기
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = {k} / (x - {p}) + {q}")
ax.legend()
ax.grid(True)

# 시야 범위
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# 출력
st.pyplot(fig)
