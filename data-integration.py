import pandas as pd

# Load the dataset
file_path = 'D:\\Download\\linkedin_job_postings.csv'
data = pd.read_csv(file_path)

# Suppose we split the data based on 'job_type' column
# get all the unique values in the 'job_type' column
job_types = data['job_type'].unique()

# Split the data based on 'job_type' and store in a dictionary
split_data = {}
for job_type in job_types:
    split_data[job_type] = data[data['job_type'] == job_type]

# Now, merge the data back together
combined_data = pd.concat(split_data.values(), ignore_index=True)

# Check the merged data
print(combined_data.info())
