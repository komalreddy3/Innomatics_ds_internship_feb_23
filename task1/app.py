import streamlit as st
st.title("_:red[My First Streamlit Data App]_ :desktop_computer:")
st.header("Analytics on Stock Data")
st.caption("Created by Komal Reddy K")
#st.caption("From Telangana")
btn_click=st.button("Click me to get insight on finance :eye: ")
##st.write(btn_click)
if btn_click==True:
    st.subheader("You clicked me :wave:")
    st.text('Finance is essentially an umbrella term for housing several aspects of money, it  ')
    st.text('can be broadly stated as the study of the matter regarding creation, management, ')
    st.text('and study of currency, money, and capital assets.')
    st.subheader("This is the general idea about the topic I chose :ok_hand:") 
st.subheader('For the analysis visualisations go to the pages on the :point_left: ')