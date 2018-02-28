
import os
import pandas as pd


from datetime import datetime

WL1_timestamp1 = "2017-12-07 14:10:51"
WL2_timestamp2 = "2017-12-07 15:43:34"

t1 = datetime.strptime(WL1_timestamp1, "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(WL2_timestamp2, "%Y-%m-%d %H:%M:%S")


path = "2017-12-07_hr_sdb_sdb_db_event_timers.tsv"



df = pd.read_table(path, sep='\t', low_memory=False)
cols = list(df)
print cols
df1 = df[df['dbNode']=="sdb1-1"]
df2 = df[df['dbNode']=="sdb1-2"]
df3 = df[df['dbNode']=="sdb1-3"]
event_types = df['sdb_db_event_timers.component'].unique()

print event_types

#for event in event_types:
#	print event
	#c1[event] = df1[df1['sdb_db_event_timers.component'] == event].count()
	#c2[event] = df2[df2['sdb_db_event_timers.component'] == event].count()
	#c3[event] = df3[df3['sdb_db_event_timers.component'] == event].count()
#print("DF1= ")
#print(df1.groupby(['sdb_db_event_timers.component']).size())
#print("DF2= ")
#print(df2.groupby(['sdb_db_event_timers.component']).size())
#print("DF3= ")
#print(df3.groupby(['sdb_db_event_timers.component']).size())



print("-----------------------------------------------------------------")


c1 = df1[df1['sdb_db_event_timers.component'] == "catsrv"]
c2 = df2[df2['sdb_db_event_timers.component'] == "catsrv"]
c3 = df3[df3['sdb_db_event_timers.component'] == "catsrv"]


print(c1.groupby(['sdb_db_event_timers.category']).size())
print(c2.groupby(['sdb_db_event_timers.category']).size())
print(c3.groupby(['sdb_db_event_timers.category']).size())
