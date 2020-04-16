# pattern
"""
1
22
333
4444
55555
"""

for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
print("==================")
for k in range(1,6):
    for l in range(k):
        print(l,end="")
    print()
print("------------------")
for m in range(1,6):
    for n in range(m-1):
        print(m,end="")
    print()
print("------------------")
for m in range(1,6):
    for n in range(m+1):
        print(m,end="")
    print()
print("------------------")
for m in range(1,6):
    for n in range(m+1):
        print(n,end="")
    print()
