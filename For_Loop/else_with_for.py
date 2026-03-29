name = ["Prateek", "Ishika", "Yadav"]

for i in name:
    print(i)
    if i=="Ishika":
        break
else:
    print("This Ittresion Is Successfull Run")
    
    
    
# check number prime number or not

number = int(input("Print Number For check Number is prime or not : "))

for i in range(2,number):
    if (number % i) == 0:
        print(number,"is not a prime number")
        break
else:
    print(number,"is a prime number")
    
  
# print N prime Number  
for i in range(number*3):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        print(i)
        


