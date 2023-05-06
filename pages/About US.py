import streamlit as st
from send_email import send_email
import pandas

st.set_page_config(layout="wide")
st.header("Contact Me")

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    option =  st.selectbox("Select The Topic", df['topic'])
    raw_message = st.text_area("Your Message Here")

    message = f"""\
Subject: New email From: {user_email}

{raw_message}

Topic: {option}

From: {user_email}

"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your Email was Sent")

