import streamlit as st

st.title("🏠 1. Home")

st.header("Banquet Hall Data Wrangling")

st.write("""
Data wrangling means preparing raw data so that it can be used for
analysis. In this project, we use a banquet hall booking dataset and
perform simple data-wrangling operations.
""")

st.subheader("Project Objectives")

st.write("1. Load a CSV file using Pandas.")
st.write("2. Check the number of rows and columns.")
st.write("3. Find missing values.")
st.write("4. Remove duplicate records.")
st.write("5. Fill missing values.")
st.write("6. Understand class imbalance.")
st.write("7. Balance the data using simple oversampling.")
st.write("8. Create basic charts.")

st.subheader("Dataset Columns")

st.table({
    "Column": [
        "Booking_ID", "Event_Type", "Guest_Count", "Planning_Hours",
        "Hall_Occupancy", "Service_Rating", "Satisfaction_Score",
        "Review_Result"
    ],
    "Meaning": [
        "Booking number", "Type of event (Wedding, Corporate, etc.)",
        "Number of guests", "Hours spent planning the event",
        "Hall occupancy percentage", "Service quality rating",
        "Customer satisfaction marks", "Satisfied or Unsatisfied"
    ]
})

st.success("Go to Page 2 to load and inspect the data.")
