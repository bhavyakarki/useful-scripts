import os
import pandas as pd
from scipy import stats

print("hi")
path1 = "./WL1/"
path2 = "./WL1throttleon/"

filesA = os.listdir(path1)
filesB = os.listdir(path2)
#print(len(files))

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

for i,current in enumerate(filesA):
	#print str(i)+"= ",current
	filesA[i] = path1+filesA[i]
	filesB[i] = path2+filesB[i]
	df1 = pd.read_table(filesA[i], sep='\t', low_memory=False)
	df1_test = df1.select_dtypes(include=numerics)
	print filesA[i] + " = " + str(df1.shape)
	df2 = pd.read_table(filesB[i], sep='\t', low_memory=False)
	df2_test = df2.select_dtypes(include=numerics)
	print filesB[i] + " = " + str(df2.shape)
	#print filesB[i]
	#print len(df.columns)
	#ne = (df1 != df2).any(1)
	l1 = list(df1._get_numeric_data())
	l2 = list(df2._get_numeric_data())
	print("WL1: ", len(l1))
	print("WL2: ",len(l2))
	#assert(l1==l2)
	#print("--------------------------------------------------")
	#ne = (df1 != df2).any(1)
	#print "diff = ", ne
	#if l1 != l2:
	#    print "Gone!"
    #print current
	for j in range(len(l1)):
	    try:
	        listA = df1_test[l1[j]]
	    
	        listB = df2_test[l1[j]]
	    
	        pval = stats.ttest_ind(listA,listB, nan_policy='omit')[1]
	        print l1[j] + " = " + str(pval)
	    except:
	        print "_________________________", l1[j]
		 	    	
	print("--------------------------------------------------")

