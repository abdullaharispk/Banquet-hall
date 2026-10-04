import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 5. Data Visualization")

df = pd.read_csv("data/banquet_data.csv")

# Simple cleaning
df = df.drop_duplicates()
df["Planning_Hours"] = df["Planning_Hours"].fillna(df["Planning_Hours"].mean())
df["Service_Rating"] = df["Service_Rating"].fillna(
    df["Service_Rating"].mean()
)
df["Event_Type"] = df["Event_Type"].fillna(df["Event_Type"].mode()[0])

st.subheader("1. Satisfied and Unsatisfied Bookings")

result_count = df["Review_Result"].value_counts()

fig, ax = plt.subplots()
result_count.plot(kind="bar", ax=ax)
ax.set_xlabel("Review Result")
ax.set_ylabel("Number of Bookings")
ax.set_title("Satisfied vs Unsatisfied Bookings")
st.pyplot(fig)

st.subheader("2. Planning Hours")

fig, ax = plt.subplots()
ax.hist(df["Planning_Hours"], bins=8)
ax.set_xlabel("Planning Hours")
ax.set_ylabel("Number of Bookings")
ax.set_title("Planning Hours Distribution")
st.pyplot(fig)

st.subheader("3. Hall Occupancy vs Satisfaction Score")

fig, ax = plt.subplots()
ax.scatter(df["Hall_Occupancy"], df["Satisfaction_Score"])
ax.set_xlabel("Hall Occupancy")
ax.set_ylabel("Satisfaction Score")
ax.set_title("Hall Occupancy vs Satisfaction Score")
st.pyplot(fig)

st.subheader("4. Service Rating vs Satisfaction Score")

fig, ax = plt.subplots()
ax.scatter(df["Service_Rating"], df["Satisfaction_Score"])
ax.set_xlabel("Service Rating")
ax.set_ylabel("Satisfaction Score")
ax.set_title("Service Rating vs Satisfaction Score")
st.pyplot(fig)

st.subheader("5. Satisfaction Score Distribution")

fig, ax = plt.subplots()
ax.boxplot(df["Satisfaction_Score"])
ax.set_ylabel("Satisfaction Score")
ax.set_title("Satisfaction Score Box Plot")
st.pyplot(fig)

st.subheader("Simple Observations")

st.write(
    "• The bar chart shows how many bookings were satisfied and unsatisfied."
)
st.write(
    "• The histogram shows how planning hours are distributed."
)
st.write(
    "• The scatter plots help us understand relationships between variables."
)
st.write(
    "• The box plot helps us understand the spread of satisfaction scores."
)

st.success("Project completed! You have now performed a basic data-wrangling workflow.")
