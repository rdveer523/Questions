# merging dictionaries
#https://towardsdatascience.com/merging-dictionaries-in-python-3-9-3b0409aa91a8
#------------------------------------------------

d1 = {'name': 'Tom', 'age': 20}
d2 = {'gpa': 4.0, 'is_single': True}
dnew = dict()
for key, value in d1.items():
    dnew[key] = value
for key, value in d2.items():
    dnew[key] = value
print(dnew)
#_------------------------------------------
dn1={}
for i,j in d1.items() & d2.items():
    dn1[i]=j
print(dn1)
#------------------------------------
dn2=dict()
for k,l in d1.items() | d2.items():
    dn2[k]=l
print(dn2)
