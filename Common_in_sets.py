#Common elements in sets
#----------------------------
s1 = {1,2,3,4,5}
s2={4,5,6,7}

#common
print(s1 & s2)
print(s1.intersection(s2))

#all
print(s1 | s2)
print(s1.union(s2))

#
print(s1.add('ve'))
#
s3=s1.copy()
print("removed all elements in s1 : ",s1.clear())
#
print("s3 copied from s1:, ",s3)
#
print("using AND operator", s2 and s3)
print("using OR operator : ", s2 or s3)
#
print("Difference of two sets i.e. except common elements in both : ",
      s3.difference(s2))
