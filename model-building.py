import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# Load the dataset
file_path = 'sorted_job_frequency.csv'
data = pd.read_csv(file_path)
# Standardize the 'frequency' feature
scaler = StandardScaler()
data['frequency_scaled'] = scaler.fit_transform(data[['frequency']])
# Determine the optimal number of clusters k for KMeans using the Elbow method
wcss = []
for i in range(1, 11):  # Test for k values from 1 to 10
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data[['frequency_scaled']])
    wcss.append(kmeans.inertia_)
# Plot the elbow graph
plt.figure(figsize=(10, 8))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Within-cluster Sum of Squares (WCSS)')
plt.show()
# optimal k is 3
optimal_k = 4
# Now fit the KMeans model with the optimal k and make cluster assignments
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=42)
data['cluster'] = kmeans.fit_predict(data[['frequency_scaled']])
# Save the clustered data to a CSV file for further analysis
output_csv_path = 'clustered_data.csv'
data.to_csv(output_csv_path, index=False)

print(f"Clustered data saved to {output_csv_path}")
