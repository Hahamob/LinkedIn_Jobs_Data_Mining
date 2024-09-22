import pandas as pd

# Load the dataset
file_path = 'D:\\Download\\linkedin_job_postings.csv'
data = pd.read_csv(file_path)

# Handling Missing Values
# Check for missing values in each column
print(data.isnull().sum())
# Choose to drop rows with any missing values
data_cleaned = data.dropna()

# Check the cleaned DataFrame
print(data_cleaned.info())
