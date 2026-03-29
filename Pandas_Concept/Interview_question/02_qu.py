"""
20 Data Analytics Theoretical Questions with Answers + Python Examples
"""

# 1. What is Data Analytics?
# Answer: Data analytics is the process of analyzing raw data to get insights.

# Example:
import pandas as pd
import numpy as np

# 2. Difference between Data Analytics and Data Science
# Example not needed (conceptual)

# 3. Steps of Data Analysis Process
# Example (simple data flow):
data = pd.DataFrame({"A": [1,2,3], "B":[4,5,6]})
print("Sample Data:\n", data)

# 4. What is EDA?
# Example: Describe dataset
print("\nDescribe Data:\n", data.describe())

# 5. Data Cleaning Libraries in Python
# Example: Checking missing values
print("\nMissing Values:\n", data.isnull().sum())

# 6. Handling Missing Values
# sample = pd.DataFrame({"Age": [20, None, 30]})
# print("\nBefore Fillna:\n", sample)
# sample_filled = sample.fillna(sample["Age"].mean())
# print("After Fillna:\n", sample_filled)

# 7. loc vs iloc
# print("\nloc Example:", data.loc[0])
# print("iloc Example:", data.iloc[0])

# 8. What is DataFrame?
# Already shown via examples.

# 9. Reading CSV
# Example (commented):
# df = pd.read_csv('file.csv')

# 10. GroupBy Example
# sales = pd.DataFrame({"City": ["A", "A", "B"], "Amount": [100,200,300]})
# print("\nGroupBy Sum:\n", sales.groupby("City")["Amount"].sum())

# 11. Mean, Median, Mode
# nums = [10, 20, 20, 30]
# print("\nMean:", np.mean(nums))
# print("Median:", np.median(nums))
# from statistics import mode
# print("Mode:", mode(nums))

# 12. Correlation
# print("\nCorrelation:\n", sales.corr(numeric_only=True))

# 13. Heatmap (commented, visualization)
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.heatmap(sales.corr(), annot=True)
# plt.show()

# 14. Outlier
# Example using IQR
# df_out = pd.DataFrame({"Score": [10,12,15,14,300]})
# Q1 = df_out.Score.quantile(0.25)
# Q3 = df_out.Score.quantile(0.75)
# IQR = Q3 - Q1
# outliers = df_out[(df_out.Score < Q1 - 1.5*IQR) | (df_out.Score > Q3 + 1.5*IQR)]
# print("\nOutliers:\n", outliers)

# 15. Outlier Detection Methods – already shown

# 16. Normalization
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# normalized = scaler.fit_transform(df_out)
# print("\nNormalized Data:\n", normalized)

# # 17. Standardization
# from sklearn.preprocessing import StandardScaler
# std = StandardScaler().fit_transform(df_out)
# print("\nStandardized Data:\n", std)

# 18. SQL vs Pandas (conceptual)

# 19. Types of Data (conceptual)

# 20. Visualization Tools (conceptual examples available above)

print("\nFile execution completed!")
