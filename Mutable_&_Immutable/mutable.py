list_1=[1,2,3,4]
list_2=list_1

print(f"List_1 : {list_1}\nList_2 : {list_2}")
print("")

list_1[0]="one"
print(f"List_1 : {list_1}\nList_2 : {list_2}")
print("")

list_2[1]="two"
print(f"List_1 : {list_1}\nList_2 : {list_2}")
print("")

list_1="Jai Shree Ram"
print(f"List_1 : {list_1}\nList_2 : {list_2}")
print("")

l1=[1,2,3,4]
l2=l1.copy()
l3=l1[:]
print(f"l1 : {l1}\nl2 : {l2}\nl3 : {l3}")
print("")

l1[0] = "one"
print(f"l1 : {l1}\nl2 : {l2}\nl3 : {l3}")