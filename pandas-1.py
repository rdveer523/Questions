"""
25. What is pandas?
Pandas is an open source python library which has a very rich set of
data structures for data based operations. Pandas with it’s cool features
fits in every role of data operation, whether it be academics or
solving complex business problems. Pandas can deal with a large variety of
files and is one of the most important tools to have a grip on.
"""
print("------------------")
"""
26. What are dataframes?
A pandas dataframe is a data structure in pandas which is mutable. Pandas has
support for heterogeneous data which is arranged across two axes.( rows and
columns).

Reading files into pandas:-

Import pandas as pd
df=pd.read_csv(“mydata.csv”)

Here df is a pandas data frame.
read_csv() is used to read a comma delimited file as a dataframe in pandas.
"""
print("------------------")
"""
27. What is a pandas Series?
Series is a one dimensional pandas data structure which can data of almost
any type. It resembles an excel column. It supports multiple operations and
is used for single dimensional data operations.

Creating a series from data:
"""
import pandas as pd

data = [1,'v',3.0]
ser = pd.Series(data)
print(ser)
print(type(ser))

print("------------------")
"""
28. What is pandas groupby?
A pandas groupby is a feature supported by pandas which is used to split and
group an object. Like the sql/mysql/oracle groupby it used to group data by
classes, entities which can be further used for aggregation. A dataframe can
be grouped by one or more columns.
"""
df1 = pd.DataFrame({'Vehicle':['Avenger','Maruthi','Fortuner','Jaguar','Airways'],
                    'Type':['bike','car','car','car','plane']})
print(df1)
print(df1.groupby('Type').count())

print("------------------")
"""
29. How to create a dataframe from lists?
To create a dataframe from lists ,
1)create an empty dataframe
2)add lists as individuals columns to the list
"""
print("------------------")
"""
30. How to create dataframe from a dictionary?
A dictionary can be directly passed as an argument to the DataFrame() function
to create the data frame.
"""
places=['Guntur','Nuzvid','Narasaraopet','Hyderabad','Pune','Noida']
states=['AP','AP','AP','TS','MH','UP']
d1={'place':places,'state':states}
df3=pd.DataFrame(d1)
print(df3)
