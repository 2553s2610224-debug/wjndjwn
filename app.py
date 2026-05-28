import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="연애 확률 테스트",
    page_icon="💘"
)

st.title("💘 연애 확률 테스트")
st.write("이름을 입력하면 연애 성공 확률을 알려드립니다!")

name = st.text_input("이름 입력")

def love_probability(name):
    # 이름 기반 고정 랜덤값 생성
    hash_value = hashlib.md5(name.encode()).hexdigest()
    seed = int(hash_value, 16)

    random.seed(seed)

    return random.randint(1, 100)

if st.button("확률 보기"):

    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        percent = love_probability(name)

        st.subheader(f"{name}님의 연애 확률은?!")

        st.progress(percent)

        st.success(f"❤️ {percent}% ❤️")

        if percent >= 80:
            st.balloons()
            st.write("연애 고수네요 😎")

        elif percent >= 50:
            st.write("좋은 인연이 찾아올 가능성이 높아요 😊")

        else:
            st.write("아직은 때가 아닐지도...? 😅")
