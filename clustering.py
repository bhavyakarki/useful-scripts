import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

features = pd.read_csv("./segmented_file/WL1_combined.csv")


# forcely pre-processing 
features = features.apply(pd.to_numeric, errors='coerce')
features = features.dropna(axis=1)
features = features.transpose()
features = features[features.sum(axis=1) > 0.0]
features = features[features.std(axis=1) > 0.0]

mean = features.mean(axis=1)
std = features.std(axis=1)

features = features.sub(mean, axis=0)
features = features.div(std, axis=0)
features = features.as_matrix()

#model 
kmeans = KMeans(n_clusters=10, random_state=0).fit(features)
print(kmeans.labels_)

# pca before visualization
pca = PCA(n_components=2)
shaped = pca.fit_transform(features)

plt.scatter(shaped[:, 0], shaped[:, 1], c=kmeans.labels_)
plt.xlim(-2, -1.3)
plt.show()
