# Banquet Hall Data Wrangling

## Beginner Mini Project

This is a simple Data Wrangling project created using:

- Python
- Pandas
- Matplotlib
- Streamlit

## Pages

### Page 1 — Home
Introduction and objectives.

### Page 2 — Load Data
Learn:
- `read_csv()`
- `head()`
- `shape`
- `dtypes`
- `isnull()`
- `describe()`
- `duplicated()`

### Page 3 — Clean Data
Learn:
- `drop_duplicates()`
- `fillna()`
- `mean()`
- `mode()`

### Page 4 — Balance Data
Learn:
- `value_counts()`
- Class imbalance
- Random oversampling
- `sample()`
- `concat()`

### Page 5 — Charts
Learn:
- Bar chart
- Histogram
- Scatter plot
- Box plot

## Installation

Install Python 3.10 or newer.

Open Command Prompt/Terminal in this project folder.

Run:

```bash
pip install -r requirements.txt
```

Then run:

```bash
streamlit run app.py
```

## Dataset

The supplied banquet hall booking dataset intentionally contains:

- Missing values
- Duplicate rows
- An imbalanced Review_Result column (Satisfied vs Unsatisfied)

This allows students to practice data-wrangling concepts.

## Important

This is an educational project. The balancing technique is demonstrated
to explain the concept of random oversampling. In a real machine-learning
project, balancing is normally performed on training data after splitting
the dataset.
