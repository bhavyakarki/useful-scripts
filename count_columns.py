
import os
import pandas as pd

print("hi")
path = "./WL1"

files = os.listdir(path)
#print(len(files))
for i,current in enumerate(files):
	print str(i)+"= ",current
	df = pd.read_table(current, sep='\t', low_memory=False)

	print len(df.columns)
