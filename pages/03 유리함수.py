import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="유리함수 y = k/(x - p) + q", layout="centered")

# 💠 배경색 설정 (#d4f4ff)
page_bg_color = """
<style>
body {
    background-color: #d4f4ff;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# 제목
st.title("💡 유리함수 시각화: y = k / (x - p) + q")

# 개념 설명
st.markdown("""
**유리함수(Rational Function)**의 대표적인 형태 중 하나는 다음과 같습니다:

### 👉  y = k / (x - p) + q

- **k** : 그래프의 모양(대칭 방향과 기울기)을 결정  
- **p** : **수직 점근선**의 위치를 결정 (x = p)  
- **q** : **수평 점근선**의 위치를 결정 (y = q)  

이 함수는 x = p에서 정의되지 않으며,  
그래프는 두 개의 분리된 가지로 구성됩니다.
""")

# 🎛️ 슬라이더 설정
st.sidebar.header("⚙️ 함수 계수 조절")
k = st.sidebar.slider("k (분자의 계수)", -10.0, 10.0, 1.0, step=0.1)
p = st.sidebar.slider("p (수직 점근선 위치)", -50.0, 50.0, 0.0, step=0.5)
q = st.sidebar.slider("q (수평 점근선 위치)", -50.0, 50.0, 0.0, step=0.5)

# x 값 설정
x = np.linspace(-100, 100, 2000)

# 분모가 0이 되는 점 제외
mask = (x - p) != 0
y = np.zeros_like(x)
y[mask] = k / (x[mask] - p) + q

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x[mask], y[mask], color='blue', label="y = k / (x - p) + q")

# 점근선 표시 (넓은 범위)
ax.plot([p, p], [-100, 100], color='red', linestyle='--', label=f"수직 점근선: x = {p:.2f}")
ax.plot([-100, 100], [q, q], color='green', linestyle='--', label=f"수평 점근선: y = {q:.2f}")

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
