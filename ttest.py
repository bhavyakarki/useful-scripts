import pandas as pd
from scipy.stats import ttest_ind


df = pd.read_csv('WL1_merged.csv')
output = open('WL1_ttest.csv', 'w')

test_A = df[df['Group']=='WL1_on']
test_B = df[df['Group']=='WL1_off']

cols = df.columns
num_cols = df._get_numeric_data().columns

for col in num_cols:
    t_value, p_value = ttest_ind(test_A[col], test_B[col], nan_policy='omit')
    output.write(str(col)+","+str(t_value)+","+str(p_value)+"\n")
output.close()
