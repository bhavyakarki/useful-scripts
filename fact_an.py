import os
import pandas as pd
import time
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA, FactorAnalysis
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 


df = pd.read_csv("/Users/bhavyakarki/Downloads/snapshots/Dec_8th/WL1_combined.csv")
print len(df.columns)
df.drop(['dbDC', 'Unnamed: 0', 'dbId'], axis=1, inplace=True)
#print df.columns
dbdc = df.filter(like='dbDC')
#print dbdc
df.drop(dbdc.columns, axis=1, inplace=True)
#print df.columns

unnamed = df.filter(like='Unnamed: 0')
df.drop(unnamed.columns, axis=1, inplace=True)
#print df.columns

dbid = df.filter(like='dbId')
df.drop(dbid.columns, axis=1, inplace=True)


colldate = df.filter(like='CollectionDate', axis=1)
df.drop(colldate.columns, axis=1, inplace=True)

dbnode = df.filter(like='dbNode.')
df.drop(dbnode.columns, axis=1, inplace=True)

tstep = df.filter(like='timestamp.')
df.drop(tstep.columns, axis=1, inplace=True)


print (len(df.columns))

orig = df
unchanged = []
for column in df:
	if len(df[column].unique()) == 1:
		unchanged.append(column)

print len(unchanged)
print "-----"
#print df['vmstat.workingset_nodereclaim']
strcols = df.loc[:, df.dtypes == object]
#df_str =  df[[strcols]]
#print strcols
print "-----"
n=0
str_unchanged = []
for c in strcols:
	if c in unchanged:
		n += 1
		str_unchanged.append(c)
orig.drop(orig[str_unchanged], axis=1, inplace=True)
new_strcols = orig.loc[:, df.dtypes == object]

#print new_strcols.columns
mapping = {'sdb1-1': 1, 'sdb1-2': 2, 'sdb1-3' : 3}
#new_strcols.dbNode.map(dict(sdb1-3=3, sdb1-2=2, sdb1-1=1))
orig.replace({'dbNode': mapping}, inplace=True)
#print orig['dbNode']
mapping = {'cs999-1-dfw.ops.sfdc.net': 1, 'cs999-2-dfw.ops.sfdc.net': 2, 'cs999-3-dfw.ops.sfdc.net' : 3}

orig.replace({'sdb_global_info.host.hostname':mapping}, inplace=True)
#print orig['sdb_global_info.host.hostname']
mapping = {'on': 1, 'off': 0}
orig.replace({'sdb_config.transaction_read_only':mapping, 'sdb_config.use_disk_backed_hashed_subplan': mapping}, inplace=True)
orig.drop(['sdb_global_info.host.hostname'], axis=1, inplace=True)
orig['timestamp'] = pd.to_datetime(orig['timestamp'])
print orig.columns
print "------------"
orig.drop(['meminfo.minuteSinceMidnight.1', 'timestamp'], axis=1,inplace=True)
orig.dropna(inplace=True, how='all')
'''
x = orig.values

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df2 = pd.DataFrame(x_scaled)
print df2
'''
for col in orig:
	orig[col]=(orig[col]-orig[col].mean())/orig[col].std()
orig = orig.fillna(0)


#print orig
print orig.columns
X=orig.values
n_rows, n_cols = X.shape
y = orig.columns
pca = PCA().fit(X)
print 'Explained variance by component: %s' % pca.explained_variance_ratio_
print len(pca.components_)


'''
binner = Bin(bin_start=1, axis=0)
binned_matrix = binner.fit_transform(X)
shuffle_indices = get_shuffle_indices(X.shape[0])


shuffled_matrix = binned_matrix[shuffle_indices, :]

'''
print "FA STARTS.........", X.shape
fa_model = FactorAnalysis().fit(X)
print fa_model.get_covariance().shape
#df_plot = pd.DataFrame(fa_model.components_, columns=y)
#df_plot.plot.scatter(s= df_plot['timestamp'])
pd.plotting.scatter_matrix(orig, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
