import os
import pandas as pd


path = "./WL1"

files = os.listdir(path)
print(len(files))
for current in files:
	print current
