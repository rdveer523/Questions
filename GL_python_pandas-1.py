#Great Learning Python Questions:
#29. How to create a dataframe from lists?
#-------------------------------------------
import numpy as np
import pandas as pd

df = pd.DataFrame()
l1 = ['amma','nanna','me','brother']
l2 = ['soft','harsh','soft','soft']
l3 = ['houseWife','carpenter','UnEmpl','soft_Eng']
l4 = ['Guntur','Guntur','Noida','Hyderabad']
l5 = ['Saver','Earner','Nill','Earner']
l6 = [50,58,34,31]

df['Family'],df['Age'],df['Behavior'],df['living'],df['job'],df['work']=l1,l6,l2,l4,l3,l5
print(df)

#------------------------------------------------
#30. How to create dataframe from a dictionary?
d1 = {'Famliy':l1, 'Age':l6}
dd1 = pd.DataFrame(d1)
print(dd1)

#------------------------------------------------
#31. How to create a new column in pandas by using values from other columns?
# example: calculations
n1 = [3,2,1]
n2 = [7,7,7]
#mul1 = pd.DataFrame({'A':n1,'B':n2,'*':n1*n2})
mul1 = pd.DataFrame()
mul1['A'],mul1['B']=n1,n2
mul1['*']=mul1['A']*mul1['B']
print(mul1)
#-------------------------------------------------------
