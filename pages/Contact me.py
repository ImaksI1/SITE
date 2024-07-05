import streamlit as st
from send_email import *

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress")
    message = st.text_area("Write your message")
    button = st.form_submit_button("Submit")
    if button:
        SendEmail(f"{user_email}\n{message}")
        st.info("Your email has been sent successfully")
        file = open("file.csv", "r")
        file_buffer = file.read()
        file.close()
        file = open("file.csv", "w")
        file.write(f"{file_buffer}{user_email}, {message}\n")
        file.close()



