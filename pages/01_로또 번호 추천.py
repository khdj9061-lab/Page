import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="로또 번호 추첨기", page_icon="🎱")

# 제목
st.title("🎱 로또 번호 추첨기")

st.write("원하는 세트 수를 정하고, 1~45 사이의 숫자 중 랜덤으로 6개씩 추첨해보세요!")

# ✅ 세트 수 입력
num_sets = st.slider("추첨할 세트 수를 선택하세요", min_value=1, max_value=20, value=5)

# ✅ 버튼 클릭 시 추첨
if st.button("추첨하기 🎰"):
    st.subheader("✨ 추첨 결과 ✨")
    for i in range(num_sets):
        numbers = sorted(random.sample(range(1, 46), 6))
        # 결과를 예쁘게 출력
        st.markdown(f"**세트 {i+1}:**  " + " 🎯 ".join([f"`{n}`" for n in numbers]))

st.markdown("---")
st.caption("💡 각 세트는 중복 없이 1~45 사이의 6개 번호를 무작위로 추첨합니다.")
