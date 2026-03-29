#        *                *
#       ***              ***            
#        e              *****
#        e                e
#        e                e
#        e                e
#        e                e
#       ***               e
#                         e
#                         e
#                       *****


n=3
a=n+2
b=n+1
c=b//2
# print(c)
# c=n-2

if n<=2 or n%2==0:
    print("Please Enter The Odd Number Which is >=3")
else:
    for i in range(c):
        for j in range(c-i,1, -1):
            print(" ", end="")
            
        for k in range(i*2+1):
            print("*", end="")
            
        print("")