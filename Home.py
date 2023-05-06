import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.header("The Company Website")
content = """
A company is an entity that has a separate legal existence from its owners.
 The owners of the company are known as members or shareholders.
 Every company must have at least one member.31-Oct-2022
Starting a small business company | ASIC
 › for-business › starting-a-small-abusing...
Search for: What does being a company mean?
What's the difference between company and company?
In the conclusion now we know that a company is a singular noun, 
companies is a plural noun, company's is singular 
possessive noun and companies' is plural possessive noun.01-Jan-2021

"""
st.info(content)
st.subheader("OUR TEAM")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(row['first name'] + row['last name'])
        st.write(row['role'])
        st.image('images/' + row['image'])


with col2:
    for index, row in df[4:8].iterrows():
        st.header(row['first name'] + row['last name'])
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row['first name'] + row['last name'])
        st.write(row['role'])
        st.image('images/' + row['image'])
