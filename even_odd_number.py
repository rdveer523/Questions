#eevn or odd
#-----------------


def even_odd(n1):
    if n1%2==0:
        print(n1, "is an EVEN Number")
    elif n1%2==1:
        print(n1, "is an ODD Number")
    else:
        print("Please give a valid number")
    print("Quotient is ", n1/2)
    
even_odd(int(input("Give any number : ")))
