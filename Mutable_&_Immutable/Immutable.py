# Immutable : the datatype which is not changeble 
# Exp : String, Number, Tuple, Boolean

# when we create a immutable variable/ datatype {e.g. string} then python create a memory/referance in ram for the string/object {eg. var_1 = "Shree Ram"}
# and if we create a new variable/datatype for the same string/value then python give the same referance, python not create a new referance/memory  {eg. var_2 = var_1}
# if we change the first variable {var_1 = "Shree Radhe"} then it create a new referance for var_1 not for var_2 because string is immutable not chageble it mean which value store in one time in one variable then it not changeble
# if we assign a new value in variable {var3="Ram" to var3="Radhe"} then first time it create a new referance in var3 when we assign a new variable in var3 then it create a new referance for var3 and first value {Ram} store in garbage for some time {python think we can use this value in next step or after some time} if we not assign then it automatic remove after some time


# var_1 = "Shree Ram"
# var_2 = var_1
# print(f"Var1 : {var_1}\nVar2 : {var_2}")

# var_1[0]="A"

# var_1 = "Shree Radhe"
# print(f"Var1 : {var_1}\nVar2 : {var_2}")

# var_3="Ram"
# print(f"Var3 : {var_3}")

# var_3="Radhe"
# print(f"Var3 : {var_3}")


