"""
How to use this script: python3 clustering.py 100 > cluster_100.txt
 change the argument to the number of clusters
"""

import sys
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import collections
import pprint

features = pd.read_csv("./fa_result.csv")

num_cluster = sys.argv[1]

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
name_list = list(features.index)

features = features.as_matrix()

#model 
kmeans = KMeans(n_clusters=int(num_cluster), random_state=0).fit(features)

feature_class = collections.defaultdict(list)
for label, feature_name in zip(kmeans.labels_, name_list):
	feature_class[label].append(feature_name)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(feature_class)

# cluster center
# print(len(kmeans.cluster_centers_))

# pca before visualization
# pca = PCA(n_components=2)
# shaped = pca.fit_transform(features)

# plt.scatter(shaped[:, 0], shaped[:, 1], c=kmeans.labels_)
# plt.xlim(-2, -1.3)
# plt.show()
