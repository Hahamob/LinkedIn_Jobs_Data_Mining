import pandas as pd

# Load the dataset
file_path = 'D:\\pythonproject\\sorted_job_frequency.csv'
data = pd.read_csv(file_path)

# Filter the DataFrame to include only those rows where frequency is greater than or equal to 500
filtered_data = data[data['frequency'] >= 500]

# Define the output file path
output_file_path = 'filtered_job_frequency.csv'

# Save the filtered data to a CSV file
filtered_data.to_csv(output_file_path, index=False)


print("The job frequency data has been sorted and saved to 'filtered_job_frequency.csv'")