"""
40. Give the below dataframe drop all rows having Nan.
"""
import pandas as pd
import numpy as np

d1={'col1':[1,2,'NaN'],'col2':['a','NaN','c']}
df1 = pd.DataFrame(d1)

d2 = {'col1':[4,5,'NaN'],'col2':['d','NaN','f']}
df2 = pd.DataFrame(d2)

df3 = pd.concat([df1,df2],axis=0)
print(df3)

#deleting row wise having NaN only
print("\n deleting row wise having NaN only \n",df3.dropna(inplace=True))
