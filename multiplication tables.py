# multiplications table
#-----------------------------

# here we should start with initialized values to variables
n1 = int(input("Enter which table you want : "))
n2 = int(input("Multiply Upto : "))
i=1
# inside the while loop, loop iterates upto i reaches the n2
while True:
    print(n1,"*",i," = ",n1*i)
    i=i+1
    if i>n2:
        break
    
