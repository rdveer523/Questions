# try the total numbers o ways reverses the elements in a list
#---------------------------------------------------------------

#l1 = [1,2,3,'a','b',2.3,(3+2j)]
# Operating System List
l1 = [3.4, 3+5j, 'Linux']
print('Original List:', l1)

print(l1[::])
# List Reverse which changes permanently
print(l1.reverse())

# updated list
print('Updated List:', l1)
print('Temporary changes : ', l1[::-1])
