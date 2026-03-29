"""
PANDAS THEORETICAL REVISION — ALL ANSWERS WITH EXPLANATORY COMMENTS
"""

import pandas as pd

# ------------------------------------------------------------
# Q1. What is a DataFrame and how is it different from a Series?
# ------------------------------------------------------------
# DataFrame: 2‑D labeled data (rows + columns)
# Series: 1‑D labeled data (single column)

# Example:
series_example = pd.Series([1, 2, 3])
dataframe_example = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})


# ------------------------------------------------------------
# Q2. Ways to create a DataFrame
# ------------------------------------------------------------
# 1. Using dictionary of lists

example_df1 = pd.DataFrame({
    "name": ["A", "B"],
    "age": [10, 15]
})

# 2. Using list of dictionaries
example_df2 = pd.DataFrame([
    {"name": "A", "age": 10},
    {"name": "B", "age": 15}
])

# 3. From list of lists
example_df3 = pd.DataFrame([
    ["A", 10],
    ["B", 15]
], columns=["name", "age"])


# ------------------------------------------------------------
# Q3. Difference between loc and iloc
# ------------------------------------------------------------
# loc  = label-based indexing (use row/column names)
# iloc = position-based indexing (use row/column numbers)

# loc example
# dataframe_example.loc[0, "col1"]

# iloc example
# dataframe_example.iloc[0, 0]



# ------------------------------------------------------------
# Q4. What does df.info() show?
# ------------------------------------------------------------
# Shows summary: column names, non-null counts, data types, memory usage.

# dataframe_example.info()


# ------------------------------------------------------------
# Q5. Difference between drop(), dropna(), fillna()
# ------------------------------------------------------------
# drop()   → remove specific rows/columns
# dropna() → remove rows/columns containing NaN values
# fillna() → replace NaN values with some value

# df.drop('col', axis=1)
# df.dropna()
# df.fillna(0)


# ------------------------------------------------------------
# Q6. Difference between merge(), join(), concat()
# ------------------------------------------------------------
# merge() → SQL-style join using columns
# join()  → join using index
# concat() → stack DataFrames vertically/horizontally

# pd.merge(df1, df2, on="id")
# df1.join(df2)
# pd.concat([df1, df2], axis=0)


# ------------------------------------------------------------
# Q7. Purpose of groupby()
# ------------------------------------------------------------
# Splits → Applies function → Combines
# Used for grouping and aggregation.

# df.groupby('city')['salary'].mean()


# ------------------------------------------------------------
# Q8. Difference between agg(), apply(), transform()
# ------------------------------------------------------------
# agg()       → multiple aggregations, reduced output size
# apply()     → apply custom function, flexible output
# transform() → output same size as input, used for group-level features

# df.groupby('city')['salary'].transform('mean')


# ------------------------------------------------------------
# Q9. reset_index() vs set_index()
# ------------------------------------------------------------
# set_index()   → make a column the index
# reset_index() → convert index back to a column

# df.set_index('id')
# df.reset_index()


# ------------------------------------------------------------
# Q10. head() vs tail()
# ------------------------------------------------------------
# head() → returns first n rows
# tail() → returns last n rows

# df.head()
# df.tail()

