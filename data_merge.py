# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:16:16 2018

@author: Hu Fan
"""

import pandas as pd
import os

path = "./"

files = os.listdir(path)

files = [f for f in files if f.endswith("tsv_t.tsv")]

count = 0
for file in files:
    if count == 0:
        df = pd.read_table(file, sep='\t', low_memory=False)
        df_combined = df
    else:
        df = pd.read_table(file, sep='\t', low_memory=False)
        df_combined_tmp = pd.concat([df_combined, df], axis=1)
        df_combined = df_combined_tmp
    count+=1
    print(df_combined.shape)
    print(file)
df_combined.to_csv('combined.csv')
    