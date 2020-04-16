# factorial
#--------------


def fact(n1):
    if n1<0:
        print("Number should be greater than 0")
    elif n1==0:
        print("0 factorial is 1")
    else:
        j=1
        for i in range(1,n1+1):
            j=i*j
        print(j)

fact(int(input("Enter factorial number :")))    
