# *args It Take The List As A Tuple Which Is Not Changble From The Function 
# If we Normally Pass The Value to any Function then It iS changeble 
# Example 
# def argsps(args):
#     args[1]="Golu"  
#     for i in args :
#         print(i)
#     print(type(args))

# a=["Prateek","vishal","Vaishali","Kuldeep","Sunita","Ishika",]
# argsps(a)
# print(type(a))

# When We Pass Any *args and **kwags Then It Mendotry That In The Parameter Block ------
# First Parameter Is Normaly,Second Parameter is *args, And Third Is **Kwags 
# Exp : def ar(n,*Args,**Kwags)

# *args ---> it is Take The List As a tuple Which Is Not Changble by The Function Its Only Fetch The Value 
# ** Kwags ---> it Is Take The Dictionary (key value)
def argsps(*args,**kwags):
    for i in args :
        print(i)

    for i,j in kwags.items():
        print(i,j)
    # print(type(args),type(disc_B))

list_a=["Prateek","vishal","Vaishali","Kuldeep","Sunita","Ishika"]
disc_B={"Prateek" : "MCA Student",
        "vishal" : "TL Of RIPL",
        "Vaishali" : "Receptionist of Mangla Hospital",
        "Kuldeep" : "Father of Prateek, Vishal, vaishali",
        "Sunita" : " House Wife Of Kuldeep ",
        "Ishika": "Ardhanani Of Prateek Yadav" }
# argsps(*list_a,**disc_B)
# print(type(list_a),type(disc_B))


print("")
# *args is use for pass the unlimited argument to the funcution

def sumFun(*args):
    sum=0
    for i in args:
        sum=sum+i
    
    return sum
    
# print(sumFun(1,2,3,4))
# print(sumFun(1,2,3,4,5,6))
# print(sumFun(1,2,3,4,5,6,7,8,9))
    
print("")

#  **kwargs it is use for give argument for the spesific parameter or it take value as a dictionery

def kwargs_fun(**kwargs):
    for i,j in kwargs.items():
        print(f"Key : {i}, value : {j}")
        
        
# kwargs_fun(Name="Prateek", Last_Name="Yadav")


