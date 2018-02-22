
import os
import pandas as pd


from datetime import datetime

WL1_timestamp1 = "2017-12-07 14:10:51"
WL2_timestamp2 = "2017-12-07 15:43:34"

t1 = datetime.strptime(WL1_timestamp1, "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(WL2_timestamp2, "%Y-%m-%d %H:%M:%S")



path = "./Dec_8th"
WL1_outpath = "./Dec_8th/WL1"


files = os.listdir(path)

# Considering only transposed files
files = [f for f in files if f.endswith("tsv_t.tsv")]
print len(files)
print files

for current in files:
	current_full = path+"/"+str(current)
	print current
	df = pd.read_table(current_full, sep='\t', low_memory=False)
	outfile = WL1_outpath+"/"+current

	
	df['timestamp'] = pd.to_datetime(df['timestamp'])
	df = df[df['timestamp'] > t1] 
	df = df[df['timestamp'] < t2]
	df.to_csv(outfile, sep='\t')
	print(df['timestamp'])

