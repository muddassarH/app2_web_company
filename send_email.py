import smtplib
import ssl
import pandas
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "muddassarhussain90@gmail.com"
    password = "zgrezriwoezcdbgr"
    receiver_email = "muddassarhussain90@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)


