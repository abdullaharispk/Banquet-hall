import streamlit as st

st.set_page_config(page_title="Banquet Hall Data", page_icon="📊")

st.title("📊 Banquet Hall Data Wrangling")
st.write("A simple beginner project using Python, Pandas and Streamlit.")

st.subheader("What will we learn?")
st.write("""
This project shows the basic steps of data wrangling:

1. Load data
2. Understand data
3. Clean data
4. Balance data
5. Create charts
""")

st.info("Use the pages in the left sidebar to go through the project step by step.")

st.subheader("Tools Used")
st.write("• Python")
st.write("• Pandas")
st.write("• Matplotlib")
st.write("• Streamlit")

st.subheader("Project Dataset")
st.write("""
The dataset contains simple banquet hall booking information such as
event type, guest count, planning hours, hall occupancy, service rating,
satisfaction score and review result.
""")
