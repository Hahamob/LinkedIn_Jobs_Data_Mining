import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
file_path = 'sorted_job_frequency.csv' 
data = pd.read_csv(file_path)

# Continue with the standardization and KMeans clustering as described before
scaler = StandardScaler()
data['frequency_scaled'] = scaler.fit_transform(data[['frequency']])

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data[['frequency_scaled']])
data['cluster'] = kmeans.labels_

# Save the results to a new CSV file
output_file_path = 'job_postings_with_clusters.csv'
data.to_csv(output_file_path, index=False)
