import streamlit as st
from send_email import *
import pandas

st.header("Contact Me")

with (st.form(key="email_form")):
    user_email = st.text_input("Your email adress")
    topics = pandas.read_csv("topics.csv")
    topic = st.selectbox("Select topic:", topics)
    raw_message = st.text_area("Write your message")
    button = st.form_submit_button("Submit")
    if button:
        message =f"""New message
from: {user_email}
topic: {topic}
message: {raw_message}
"""
        SendEmail(message)
        st.info("Your email has been sent successfully")
        file = open("file.csv", "r")
        file_buffer = file.read()
        file.close()
        file = open("file.csv", "w")
        file.write(f"{file_buffer}{message}")
        file.close()



