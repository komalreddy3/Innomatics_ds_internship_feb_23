import streamlit as st
st.title(":red[Innomatics] Data App :sunglasses:")
st.snow()
st.header("Data Science Internship")
st.subheader("Feb 2023")
CODE='''"print("Hello World")'''
st.code(CODE,language="python")
btn_click=st.button("Click me")
##st.write(btn_click)
if btn_click==True:
    st.subheader("You clicked me :cry:")
    st.balloons()