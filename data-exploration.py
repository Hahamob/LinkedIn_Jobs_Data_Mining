import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the data
file_path = 'D:\Download\linkedin_job_postings.csv'  # Update with your file path
data = pd.read_csv(file_path)
# Ensure time fields are in datetime format
data['last_processed_time'] = pd.to_datetime(data['last_processed_time'], errors='coerce')
data['first_seen'] = pd.to_datetime(data['first_seen'], errors='coerce')
# 1. Bar chart showing the distribution of job types
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='job_type')
plt.title('Distribution of Job Types')
plt.xlabel('Job Type')
plt.ylabel('Number of Postings')
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.show()
# 2. Horizontal bar chart showing top companies by job postings
company_counts = data['company'].value_counts().head(20)  # Top 20 companies
plt.figure(figsize=(10, 6))
sns.barplot(y=company_counts.index, x=company_counts.values, orient='h')
plt.title('Top 20 Companies by Job Postings')
plt.xlabel('Number of Job Postings')
plt.ylabel('Company')
plt.show()
# 3. Histogram showing job postings by job level
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='job_level')
plt.title('Number of Job Postings by Job Level')
plt.xlabel('Job Level')
plt.ylabel('Number of Postings')
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.show()


