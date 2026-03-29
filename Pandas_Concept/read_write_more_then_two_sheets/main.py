import pandas as pd

data = pd.read_excel('C:/Users/prate/Desktop/Old_Pc_Data/VS_CODE/Python_/Pandas_Concept/read_write_more_then_two_sheets/first.xlsx')

data2= data.copy()
data2.iloc[0,2]='Kanpur'

# print(data.describe())
print(data.info())
# print(data2)

# with pd.ExcelWriter('./first.xlsx') as wr:
#     data.to_excel(wr, sheet_name='Sheet1', index=False)
#     data2.to_excel(wr, sheet_name='Sheet2', index=False)