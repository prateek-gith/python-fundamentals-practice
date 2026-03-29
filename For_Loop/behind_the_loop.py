# run in terminal python

f=open('break.py')
# print first line
f.readline() 
f.readline()
f.readline()
f.readline()

# if file is read then it return '' (empty string)
f.readline()

# core work is 

# print the line by line
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()

# if line is over then it give the error (StopItration)
f.__next__()


if f == f.iter():
    print (f" f == f.iter() ")
    
if f==f.__iter__():
    print(f"f == f.__iter__()")

# f by default iter() reference ko hold krta hai 
# list or dict me aisa nhi hota hai

list_1=[1,2,3,4]
#  in this time "list_1" hold the reference of "[1,2,3,4]" not iter reference 
#  if we do list_1.__next__() it not working

I = iter(list_1)
# now I hold the reference of itration 
I.__next__()