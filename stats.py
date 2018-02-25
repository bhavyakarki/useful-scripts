import os
import pandas as pd

file_path = './segmented_file/WL1_combined.csv'  # change this

df = pd.read_table(file_path, sep = ',')

(log_num, feature_numbers) = df.shape

dbnode = df['dbNode'].unique()
subdf = {}
for node in dbnode:
	subdf[node] = df[df['dbNode'] == node]

stats = {}
for d in subdf:
	stats[d] = subdf[d].describe()
