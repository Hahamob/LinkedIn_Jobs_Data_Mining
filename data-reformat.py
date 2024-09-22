import pandas as pd

# Load the DataFrame
job_frequency = pd.read_csv('D:\\pythonproject\\job_frequency.csv')

# Sort the DataFrame by the 'frequency' column in descending order
job_frequency_sorted = job_frequency.sort_values(by='frequency', ascending=False)

#  save this sorted DataFrame back to a CSV file
job_frequency_sorted.to_csv('sorted_job_frequency.csv', index=False)

print("The job frequency data has been sorted and saved to 'sorted_job_frequency.csv'")
