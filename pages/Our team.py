import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.header("Our team")
with col2:
    st.info("The best team:)")

col3, col4, col5 = st.columns(3)
df = pandas.read_csv("data1.csv")
with col3:
    for index, row in df[:4].iterrows():
        st.header(row["role"])
        st.write(row["first name"].title(), row["last name"].title())
        st.image("images1/" + row["image"])

with col4:
    for index, row in df[4:8].iterrows():
        st.header(row["role"])
        st.write(row["first name"].title(), row["last name"].title())
        st.image("images1/" + row["image"])
with col5:
    for index, row in df[8:12].iterrows():
        st.header(row["role"])
        st.write(row["first name"].title(), row["last name"].title())
        st.image("images1/" + row["image"])
