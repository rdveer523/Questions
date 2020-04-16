#palindrome
#----------------
def pal(n1):
    n2=n1
    n3=0
    while n1>0:
        n4=n1%0
        n3=n3*10+n4
        n1 = n1//10
    if n2==n3:
        print(n3,"is a VIKATAKAVI number")
    else:
        print("Not a palindrome")
    return n1

pal(int(input("Enter a vikatakavi number : ")))
"""
n1=1221
while True:
    n4=0
    if n4==n1:
        print(n4,"is a VIKATAKAVI number")
    else:
        n2=n1%10
        n3=n2*10
        n4=n3+0


"""
