import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
df = pd.read_csv("/home/student/Downloads/sales_data_sample.csv",
encoding='latin1')
df.head()

df = df.dropna()
data = df[['QUANTITYORDERED', 'PRICEEACH', 'SALES']]
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
wcss = []
K = range(1, 11)
for k in K:
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(data_scaled)
wcss.append(kmeans.inertia_)
plt.figure(figsize=(8, 5))
plt.plot(K, wcss, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster_KMeans'] = kmeans.fit_predict(data_scaled)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data_scaled[:, 0], y=data_scaled[:, 2],
hue=df['Cluster_KMeans'], palette='viridis')
plt.title('K-Means Clustering')
plt.xlabel('Quantity Ordered (scaled)')
plt.ylabel('Sales (scaled)')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=3)
df['Cluster_Hierarchical'] = hc.fit_predict(data_scaled)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data_scaled[:, 0], y=data_scaled[:, 2],
hue=df['Cluster_Hierarchical'], palette='Set2')
plt.title('Hierarchical Clustering')
plt.xlabel('Quantity Ordered (scaled)')
plt.ylabel('Sales (scaled)')
plt.show()
