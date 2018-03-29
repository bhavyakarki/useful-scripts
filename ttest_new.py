import os
import pandas as pd
from scipy import stats

print("hi")
path1 = "./WL2_storage_cache_on/"
path2 = "./WL2_storage_cache_off/"

filesA = os.listdir(path1)
filesB = os.listdir(path2)

output = open('W2_ttest.csv', 'w')
#print(len(files))

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

for i,current in enumerate(filesA):
	#print str(i)+"= ",current
    filesA[i] = path1+filesA[i]
    filesB[i] = path2+filesB[i]
    df1 = pd.read_table(filesA[i], sep='\t', low_memory=False)
	
    print(filesA[i] + " = " + str(df1.shape))
    df2 = pd.read_table(filesB[i], sep='\t', low_memory=False)
	
    print(filesB[i] + " = " + str(df2.shape))
	
    l1 = list(df1._get_numeric_data())
    l2 = list(df2._get_numeric_data())
    print("WL1: ", len(l1))
    print("WL2: ",len(l2))
	#assert(l1==l2)
	
	#ne = (df1 != df2).any(1)
	#print "diff = ", ne
	#if l1 != l2:
	#    print "Gone!"
    #print current
    for j in range(len(l1)):
        try:
	       
            listA = df1[l1[j]]
            listB = df2[l1[j]]
	    
            pval = stats.ttest_ind(listA, listB, nan_policy='omit')[1]
            output.write(str(l1[j])+','+str(pval)+'\n')
            print(l1[j] + " = " + str(pval))
        except:
            print("_________________________", l1[j])
		 	    	
    print("--------------------------------------------------")
output.close()
