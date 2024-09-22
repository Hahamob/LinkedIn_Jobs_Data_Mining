import pandas as pd

# Load the dataset
file_path = 'D:\\Download\\linkedin_job_postings.csv'
data = pd.read_csv(file_path)

# Calculate the frequency of each job title
job_title_counts = data['job_title'].value_counts()

# Convert the job title counts to a DataFrame
job_frequency = job_title_counts.reset_index()
job_frequency.columns = ['job_title', 'frequency']

# export this job frequency DataFrame to a CSV file
output_file_path = 'D:\\pythonproject\\job_frequency.csv'
job_frequency.to_csv(output_file_path, index=False)

print(f"The job frequency data has been successfully saved to {output_file_path}")
