import pandas as pd

# Load the dataset
file_path = 'D:\\Download\\linkedin_job_postings.csv' 
data = pd.read_csv(file_path)

# Define the columns that are likely related to job popularity
columns_of_interest = [
    'job_title',  # Name of the position
    'company',    # Name of the company
    'job_type',   # Type of the position (full-time, part-time, etc.)
    'job_location',  # Geographic location of the job
    'job_level'   # Level of the position (entry-level, mid-level, senior, etc.)
]

# Create a new DataFrame with only the columns of interest
selected_data = data[columns_of_interest]

# Check the new DataFrame to ensure it contains the right columns
print(selected_data.head())  # Prints the first few rows to verify the data
