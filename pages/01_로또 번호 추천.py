import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="로또 번호 추첨기", page_icon="🎱")

# 제목
st.title("🎱 로또 번호 추첨기")

st.write("1~45 사이의 숫자 중 6개를 무작위로 추첨합니다. 게임 수를 직접 입력해보세요!")

# ✅ 게임(세트) 수 직접 입력
num_sets = st.number_input("몇 게임을 추첨하시겠어요?", min_value=1, max_value=100, value=5, step=1)

# ✅ 버튼 클릭 시 추첨 실행
if st.button("추첨하기 🎰"):
    st.subheader("✨ 추첨 결과 ✨")
    for i in range(num_sets):
        numbers = sorted(random.sample(range(1, 46), 6))
        st.markdown(f"**게임 {i+1}:**  " + " 🎯 ".join([f"`{n}`" for n in numbers]))

st.markdown("---")
st.caption("💡 각 게임은 중복 없이 1~45 사이의 6개 번호를 무작위로 추첨합니다.")
