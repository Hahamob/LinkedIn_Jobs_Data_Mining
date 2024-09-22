import pandas as pd

# Path to your CSV file
file_path = 'D:\Download\linkedin_job_postings.csv'

# Attempt to read the CSV file
try:
    data_frame = pd.read_csv(file_path)
    print("Data successfully loaded!")
    print(data_frame.head())  # Print the first few rows of the DataFrame to verify data was read correctly
except FileNotFoundError:
    print("File not found, please check the file path.")
except pd.errors.EmptyDataError:
    print("File is empty, please check the file content.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
