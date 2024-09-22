import pandas as pd
# Load the data
file_path = 'D:\Download\linkedin_job_postings.csv'  # Update with your file path
data = pd.read_csv(file_path)
# Check for basic information and data types
info = data.info()
# Check for missing values in each column
missing_values = data.isnull().sum()
# Check for any duplicate rows
duplicate_rows = data.duplicated().sum()
# Inspecting unique values in categorical columns to find irregularities
# Replace 'job_title' with the categorical column you want to inspect
unique_job_titles = data['job_title'].unique()
# Print out the results
print("Basic Data Information:")
print(info)
print("\nMissing Values by Column:")
print(missing_values)
print("\nNumber of Duplicate Rows:")
print(duplicate_rows)
# Print the outlier detection if you have numerical data
# print("\nOutlier Detection for Salary:")
# print(salary_outliers
print("\nUnique Job Titles:")
print(unique_job_titles)
