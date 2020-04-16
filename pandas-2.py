#32. What are the different functions that can be used by grouby in pandas ?
"""
grouby() in pandas can be used with multiple aggregate functions.
Ex: sum()
    mean()
    count()
    std()

Data is divided into groups based on categories and then the data
in these individual groups can be aggregated by the aforementioned functions.
"""

#33. How to combine dataframes in pandas?
"""
Two different data frames can be stacked either horizontally or vertically by
concat()
append()
join()

functions in pandas.

concat() works best when the dataframes have the same columns in basically
vertical stacking of dataframes into a single dataframe.

Append() is used for horizontal stacking of dataframes. If two tables(dataframes)
are to be merged together then this is the best concatenation function.

Join() is used when we need to extract data from different dataframes
which are having one or more common columns. The stacking is horizontal
in this case.
"""

#34. What kind of joins does pandas offer?
"""
Pandas has a
    left join,
    inner join,
    right join and
    outer join.
"""

#35. How to merge dataframes in pandas?
"""
Merging depends on the type and fields of different dataframes being merged.
If data is having similar fields data is merged along
axis 0
else they are merged along
axis 1.
"""

#36. Given the below two dataframes form a single dataframe by vertical stacking.
import pandas as pd
import numpy as np

d1={'col1':[1,2,3],'col2':['a','b','c']}
df1 = pd.DataFrame(d1)
d2 = {'col1':[4,5,6],'col2':['d','e','f']}
df2 = pd.DataFrame(d2)

concat_1 = pd.concat([df1,df2],axis=1)
"""
axis = 1 prints the two frames in a single table and indices are the same
for both colums i.e. horizantal concatenation
"""
print(concat_1)

concat_0 = pd.concat([df1,df2],axis=0)
"""
axis = 1 prints the two frames data in a single table but indices are diferent
for both columns i.e. vertical concatenation
"""
print(concat_0)
#-------------------------------------------------------
"""
38. How to select columns in pandas and add them to a new dataframe?
    What if there are two columns with the same name?
    
A)  df.columns gives the list of all columns.
    We can then form new columns by selecting columns.

If there are two column are same then copy those in a new dataframe
"""
print(concat_1.columns)
df_col1 = concat_1['col1']
print(df_column)
df_col2 = concat_1['col2']
print(df_col2)
