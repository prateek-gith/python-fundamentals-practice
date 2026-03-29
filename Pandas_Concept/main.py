import numpy as np 
import pandas as pd 

dict_1={
    "name" : ['prateek', 'vishal', 'Vaishali'],
    "age" : [25, 27, 26]
}

# pd.DataFrame(dict_1) convert dict into like excle sheet or table form with index
df = pd.DataFrame(dict_1)

# save in csv
# df.to_csv('df.csv')

# save in excel
# df.to_excel('df.xls')

# save in excel or csv without index 
# df.to_excel('df.xlsx', index=False )


# print(df)

# print two row from starting
# print(df.head(2))

# print two row from end
# print(df.tail(2))

# it collect the all numeric value from the table and display many value like : max, min, %, count etc..
# print(df.describe())

# we can read the any excel and csv file
readcsv=pd.read_csv('df.csv')
print(type(readcsv))
print(readcsv)

# display specific column 
# print(readcsv['name'])

# display specific column with row
# print(readcsv['name'][0])

# we can chaage the perticuler name 
# readcsv['name'][0]='Ishika'
# print(readcsv['name'][0])


# it return the pandas series (single column) with random value
# ser=pd.Series(np.random.randn(34))
# print(ser)
# print(type(ser))


# it return the pandas dataframe(multiple column) with random value

# pd.DataFrame(np.random.rand(NO_OF_ROW, NO_OF_COLUMN), index=np.arange(NO_OF_ROW))
newdf=pd.DataFrame(np.random.rand(8, 5), index=np.arange(8))
# print(newdf)

# return the datatype of each column
# print(newdf.dtypes)

# return the index value of dataframe 
# print(newdf.index)

# it return the column
# print(newdf.columns)


# convert row i nto column, and column into row
# print(newdf.T)

# it mean sort in ascending order behalf on row  (axis=0 mean row )
# like before row is 1,2, 3 ,4  after function 4,3,2,1
print(newdf.sort_index(axis=0, ascending=False))

# it mean sort in ascending order behalf on column  (axis=1 mean column )
# like before column is 1,2, 3 ,4  after function 4,3,2,1
print(newdf.sort_index(axis=1, ascending=False))

# We can Change the column head  name 
newdf.columns=list('ABCDE')
# print(newdf.head())

# when we want to change the value of specific shell
# newdf.loc[0,'A']=1000
# print(newdf.head())

# if we give column or row value which is not in sheet then it create new column 
# newdf.loc[0,0]=1000
# print(newdf.head())

# we can drop any column
# it mean drop the column which is name is 0 and axis=1 mean column
# note thay can't change the original dataframe
# print(newdf.drop(0, axis=1))

# we can drom more then one column or row
# print(newdf.drop(['A', 'B'], axis=1))


# if we want to drop column in my original datasheets then we add a new attribute inplace=True
# print(newdf.drop(0, axis=1, inplace=True))



# Adding a new column with a list of values
newdf['City'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# print(newdf)


# when we want to specific row and column value
# print(newdf.loc[[1,2],['B','C']])

# if we want to all row but column b,c
# print(newdf.loc[:,['B','C']])

# if we want to all column but row 1,2
# print(newdf.loc[[1,2],:])

# we can give the specific conditions
# print(newdf.loc[(newdf['A']>0.3)])


# we can give the specific more than one conditions
# print(newdf.loc[(newdf['A']>0.3) & (newdf['B']<0.3)])

# if we want to my row or column fetch with index value eighter row or column consist any value
# exp : IN THE NEWDF COLUMN NAME IS A,B,C,D but we track by index
# print(newdf.iloc[0,3])

# we can find the value of specific column
# print(newdf['A'])



# when we want to add any same value in column
# newdf.loc[:, ['B']]= 5656.00

# print(newdf)


