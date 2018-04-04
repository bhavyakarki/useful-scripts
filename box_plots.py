import os
import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# main_directory = "./segmented_file"   # change this
# files = os.listdir(main_directory)

# for file in files:
# 	file_path = main_directory+"/"+file
# 	df = pd.read_table(file_path, sep=',')
# 	(log_num, feature_numbers) = df.shape
# 	print(file+"\t"+str(feature_numbers))
# # normal


file1 = pd.read_csv('./segmented_file/WL2_off_combined.csv')  # change this
file2 = pd.read_csv('./segmented_file/WL2_on_combined.csv')
file_important = pd.read_excel('./W2_ttest.xlsx', sheet_name=None)
file_important = file_important['W2_ttest']
file_important = file_important.dropna()
file_important = file_important[file_important['Pvalue'] != '--']
file_important['Pvalue'] = file_important['Pvalue'].astype('float64')
file_important = file_important[file_important['Pvalue'] < 0.05]
for i in range(file_important.shape[0]):
	tmp = file_important['FeatureName'][i]

	if tmp in file1:
		# stats1 = file1[tmp].describe()
		# stats2 = file2[tmp].describe()
		stats1 = file1[tmp]
		stats2 = file2[tmp]
		if not stats1.isnull().values.any() and not stats2.isnull().values.any():
			print(i)
			print(tmp)
			fig = plt.figure()
			fig.tight_layout()
			plt.subplot(1,2,1)
			plt.boxplot(stats1)
			x = np.random.normal(1, 0.04, size=len(stats1))
			plt.plot(x, stats1, 'r.', alpha=0.2)
			plt.xlabel(tmp+" off",labelpad=10)
			plt.subplot(1,2,2)
			plt.boxplot(stats2)
			x = np.random.normal(1, 0.04, size=len(stats2))
			plt.plot(x, stats2, 'r.', alpha=0.2)
			plt.xlabel("on",labelpad=10)
			plt.tight_layout()
			plt.savefig(str(i)+".png")
	else:
		print(tmp)

# df = pd.read_table(file_path, sep = ',')

# (log_num, feature_numbers) = df.shape

# dbnode = df['dbNode'].unique()
# subdf = {}
# for node in dbnode:
# 	subdf[node] = df[df['dbNode'] == node]

# stats = {}
# for d in subdf:
# 	stats[d] = subdf[d].describe()

# for stat in stats:
# 	s = stats[stat]["sdb_db_event_timers.D_time [event=tcop[bind_message]]/sec"]
# 	print(s)
# 	s.plot(kind='box')
