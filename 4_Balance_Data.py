import streamlit as st
import pandas as pd

st.title("⚖️ 4. Balance Data")

df = pd.read_csv("data/banquet_data.csv")

# Clean the data first
df = df.drop_duplicates()
df["Planning_Hours"] = df["Planning_Hours"].fillna(df["Planning_Hours"].mean())
df["Service_Rating"] = df["Service_Rating"].fillna(
    df["Service_Rating"].mean()
)
df["Event_Type"] = df["Event_Type"].fillna(df["Event_Type"].mode()[0])

st.subheader("Step 1: Check Review Result Distribution")

result_count = df["Review_Result"].value_counts()

st.write(result_count)
st.bar_chart(result_count)

st.write("""
If one class has many more records than another class, the dataset is
called imbalanced.
""")

st.subheader("Step 2: Balance the Data")

satisfied_bookings = df[df["Review_Result"] == "Satisfied"]
unsatisfied_bookings = df[df["Review_Result"] == "Unsatisfied"]

st.write("Satisfied bookings:", len(satisfied_bookings))
st.write("Unsatisfied bookings:", len(unsatisfied_bookings))

if len(satisfied_bookings) > len(unsatisfied_bookings):
    small_group = unsatisfied_bookings
    large_group = satisfied_bookings
    small_name = "Unsatisfied"
else:
    small_group = satisfied_bookings
    large_group = unsatisfied_bookings
    small_name = "Satisfied"

if len(small_group) > 0:
    balanced_small_group = small_group.sample(
        len(large_group),
        replace=True,
        random_state=42
    )

    balanced_df = pd.concat(
        [large_group, balanced_small_group]
    )

    balanced_df = balanced_df.sample(
        frac=1,
        random_state=42
    ).reset_index(drop=True)

    st.subheader("After Balancing")

    st.write(balanced_df["Review_Result"].value_counts())
    st.bar_chart(balanced_df["Review_Result"].value_counts())

    st.dataframe(balanced_df.head(20), use_container_width=True)

    csv = balanced_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Balanced Data",
        csv,
        "balanced_banquet_data.csv",
        "text/csv"
    )

    st.success(
        "The smaller class was increased by randomly selecting records "
        "with replacement."
    )
else:
    st.error("The dataset does not contain both Satisfied and Unsatisfied records.")

st.info("""
### Simple idea behind balancing

Suppose we have:

Satisfied = 100 bookings  
Unsatisfied = 30 bookings

We randomly select Unsatisfied bookings again until we have approximately:

Satisfied = 100 bookings  
Unsatisfied = 100 bookings

This is called **Random Oversampling**.
""")
