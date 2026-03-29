# | Name | Age | City   |
# | ---- | --- | ------ |
# | Aman | 22  | Delhi  |
# | Rita | 17  | Mumbai |
# | John | 30  | Kanpur |

import pandas as pd

name = ['Aman', 'Rita', 'John']
age = [22,17,30]
city = ['Delhi', 'Mumbai', 'Kanpur']

data = pd.DataFrame({
    'Name' : name,
    'Age'  : age,
    'City'  : city
})

# print(data)


# print(data['Age'])
# print(data.iloc[0:1,:])
# print(data.loc[0:1,'Age'])
# print(data[['Age', 'City']])

data['Status'] = data['Age'].apply(lambda x : 'Adult' if x>=18 else 'Minor')

print(data[data['Age']>20])
# print(data)