import streamlit as st
import pandas as pd

st.title("🧹 3. Clean Data")

df = pd.read_csv("data/banquet_data.csv")

st.subheader("Before Cleaning")
st.write("Missing values:")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.write("Duplicate rows:", df.duplicated().sum())

st.subheader("Step 1: Remove Duplicate Rows")

df = df.drop_duplicates()

st.write("Rows after removing duplicates:", len(df))

st.subheader("Step 2: Fill Missing Values")

# Fill missing Planning_Hours with the average
df["Planning_Hours"] = df["Planning_Hours"].fillna(
    df["Planning_Hours"].mean()
)

# Fill missing Service_Rating with the average
df["Service_Rating"] = df["Service_Rating"].fillna(
    df["Service_Rating"].mean()
)

# Fill missing Event_Type with the most common value
df["Event_Type"] = df["Event_Type"].fillna(
    df["Event_Type"].mode()[0]
)

st.write("Missing values after cleaning:")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.subheader("Cleaned Data")
st.dataframe(df, use_container_width=True)

st.success("Cleaning completed!")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Cleaned Data",
    csv,
    "cleaned_banquet_data.csv",
    "text/csv"
)

st.info("""
### What did we do?

• Removed duplicate rows using `drop_duplicates()`  
• Filled missing Planning Hours using the mean  
• Filled missing Service Rating using the mean  
• Filled missing Event Type using the mode  
""")
