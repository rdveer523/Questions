"""
39. How to delete a columns or group of columns in pandas?
    Given the below dataframe drop column “col1”.

"""
import pandas as pd
import numpy as np

d1={'col1':[1,2,3],'col2':['a','b','c']}
df1 = pd.DataFrame(d1)
d2 = {'col1':[4,5,6],'col2':['d','e','f']}
df2 = pd.DataFrame(d2)

concat_0 = pd.concat([df1,df2],axis=0)#vertical
concat_1 = pd.concat([df1,df2],axis=1)#horizantal

print(concat_0, '\n', concat_1)

# Now deleting, use drop() method
print(concat_0.drop(['col1'],axis=1))
print(concat_1.drop(['col2'],axis=1))

# or
df3 = pd.concat([df1,df2],axis=0)
print(df3)

#dropping i.e. delete
print(df3.drop(columns=['col1']))
