import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="유리함수 그래프", layout="centered")

# 제목
st.title("유리함수 그래프 시각화")

# 개념 설명
st.markdown("""
**유리함수(Rational Function)**는 분자와 분모가 모두 일차식인 함수로,  
다음과 같은 일반적인 형태를 가집니다:

\[
y = \frac{a x + b}{c x + d}
\]

이 함수는 분모가 0이 되는 점에서 정의되지 않으며,  
그래프에는 수직 및 수평(또는 사선) 점근선이 존재할 수 있습니다.
""")

# 슬라이더 설정
st.sidebar.header("함수 계수 조절")
a = st.sidebar.slider("a (분자의 x 계수)", -10.0, 10.0, 1.0, step=0.1)
b = st.sidebar.slider("b (분자의 상수항)", -10.0, 10.0, 0.0, step=0.1)
c = st.sidebar.slider("c (분모의 x 계수)", -10.0, 10.0, 1.0, step=0.1)
d = st.sidebar.slider("d (분모의 상수항)", -10.0, 10.0, 0.0, step=0.1)

# x 값 설정
x = np.linspace(-10, 10, 1000)

# 분모가 0이 되는 점 제외
y = np.zeros_like(x)
mask = (c * x + d) != 0
y[mask] = (a * x[mask] + b) / (c * x[mask] + d)

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x[mask], y[mask], label=r"$y=\frac{a x + b}{c x + d}$", color='blue')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# 점근선 표시
if c != 0:
    asymptote_x = -d / c
    ax.axvline(asymptote_x, color='red', linestyle='--', label=f"수직점근선: x={asymptote_x:.2f}")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = ({a}x + {b}) / ({c}x + {d})")
ax.legend()
ax.grid(True)

st.pyplot(fig)
