import pandas as pd

# name = ['A', 'B', 'C']
# age  = [10, 20, 30]


# print(pd.DataFrame(
#     name,age
# ))

# | Name  | Age | City        |
# | ----- | --- | ----------- |
# | Alice | 25  | New York    |
# | Bob   | 30  | Los Angeles |
# | Carol | 22  | Chicago     |

name = ['Alice', 'Bob', 'Carlo']
age = [25,30,22]
city = ['New York', 'Los Angeles', 'Cicago']

data = pd.DataFrame({
    "Name" : name,
    "Age" : age,
    "City" : city
})

# print(type(data))
# print(data)

# print(data["Name"])
# print(data.Name)

# print(data.iloc[:2,:])
# print(data[data['Age']>24])

# data['Countery'] = "USA"
# data.drop(columns='Countery', inplace=True)


# print(data.head(1))
# print(data.tail(1))

# print(data.sort_values(by='Age', ascending=False).reset_index(drop=True))

# print(data.groupby(by='City')['Age'].mean())

# print(data.select_dtypes('int'))

data.rename(columns={'Name' : "FullName", "City":"Location"}, inplace=True)

data['AgeGroup'] = "Yong" if data['Age']>26 else "Adult"

print(data)