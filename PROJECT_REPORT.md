# Mini Project Report

## Banquet Hall Data Wrangling using Python and Streamlit

### 1. Introduction

Data wrangling is the process of collecting, cleaning and preparing data
for analysis. In this project, banquet hall booking data is processed using
simple Python programs and displayed through a Streamlit application.

### 2. Objectives

- Load banquet hall booking data.
- Understand the dataset.
- Find missing values.
- Remove duplicate records.
- Fill missing values.
- Check class imbalance.
- Balance the classes using random oversampling.
- Create basic visualizations.

### 3. Technologies Used

Python, Pandas, Matplotlib and Streamlit.

### 4. Data Cleaning

The following operations are performed:

1. Duplicate records are removed.
2. Missing Planning Hours are replaced by the mean.
3. Missing Service Ratings are replaced by the mean.
4. Missing Event Type values are replaced by the mode.

### 5. Data Balancing

The Review_Result column contains two classes: Satisfied and Unsatisfied.

If one class contains fewer records, records from the smaller class are
randomly selected with replacement until both classes have the same size.

### 6. Visualization

The project creates:

- Satisfied/Unsatisfied bar chart
- Planning Hours histogram
- Hall Occupancy vs Satisfaction Score scatter plot
- Service Rating vs Satisfaction Score scatter plot
- Satisfaction Score box plot

### 7. Learning Outcomes

After completing this project, students can:

- Read CSV files using Pandas.
- Inspect a dataset.
- Find missing values.
- Remove duplicates.
- Fill missing values.
- Understand class imbalance.
- Perform simple random oversampling.
- Create basic charts.
- Build a simple Streamlit application.

### 8. Conclusion

This project provides a beginner-friendly introduction to data wrangling.
It demonstrates how raw banquet hall booking data can be loaded, cleaned,
balanced and visualized using simple Python commands.
