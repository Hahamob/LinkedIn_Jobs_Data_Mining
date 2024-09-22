from sklearn.metrics import silhouette_score
import seaborn as sns
import pandas as pd

data = pd.read_csv('clustered_data.csv')
# 假设你的数据已经被赋予了簇标签
score = silhouette_score(data, data['cluster'])
print('Silhouette Score: %.2f' % score)

# 计算每个簇的统计描述
cluster_stats = data.groupby('cluster').agg(['mean', 'median', 'std'])
print(cluster_stats)

# 盒须图可视化
sns.boxplot(x='cluster', y='frequency', data=data)
plt.show()

# 或者小提琴图可视化
sns.violinplot(x='cluster', y='frequency', data=data)
plt.show()

