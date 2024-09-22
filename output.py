import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('clustered_data.csv')
data_filtered = data[data['cluster'] != 0]

# Visualize the clustering results using a scatter plot
sns.scatterplot(x=data_filtered.index, y='frequency', hue='cluster', palette='viridis', data=data_filtered)
plt.title('KMeans Clustering Visualization Based on Frequency')
plt.xlabel('Index')
plt.ylabel('Frequency')
plt.show()

# Calculate statistical data for each cluster
cluster_stats = data.groupby('cluster').describe()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Print the statistical data for each cluster
print(cluster_stats)


