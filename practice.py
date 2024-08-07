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
    "진행도":"80%",
    "image_url":'image/테디울.jpg'
}

with st.expander(label=label[0], expanded=False):
    st.subheader(projects["이름"])
    st.image(projects["image_url"])
    
