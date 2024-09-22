import pandas as pd

# Load the data
file_path = 'D:\Download\linkedin_job_postings.csv'
data = pd.read_csv(file_path)

# Data structure
print(data.info())

# Data quantity
print(data.shape)

# Field overview
print(data.columns)

# Surface-level features for numeric fields
print(data.describe())

# Distribution for categorical data (example for a specific categorical column)
print(data['some_categorical_column'].value_counts())

# Check for missing values
print(data.isnull().sum())
