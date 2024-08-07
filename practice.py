#!/usr/bin/env python3
import streamlit as st
import time

st.set_page_config(page_title="연수의 뜨개옷장")

st.title("연수의 뜨개옷장 :star2: ")
st.markdown("딜로이트에서 열심히 일하고 있는 연수가 streamlit을 연습하는 공간입니다!")

label = ["첫번째는 무엇일까요?"]

time.sleep(3)

projects = {
    "이름":"테디울 탑다운 가디건",
    "image_url":'image/테디울.jpg'
}

with st.expander(label=label[0], expanded=False):
    st.subheader(projects["이름"])
    st.markdown(text)
    text = """진행도는 80%. 소매 뜨고 넥밴드 뜨고 단추 달면 완성!
    """
    st.image(projects["image_url"])
    st.caption("이 가디건은 직접 입으려고 만든 것입니다.")    
