import pandas as pd
import numpy as np

df=pd.DataFrame({
    "Name" : ['Prateek', 'Vishal', 'Vaishai', np.nan, 'Prateek'],
    "Toy" : [np.nan, 'MoB', 'Bup', np.nan, 'New'],
    "Born" : [pd.NaT, pd.Timestamp("1995-06-04"), pd.NaT, np.nan,pd.Timestamp("1999-08-27") ],
    "None Value" : [pd.NaT, np.nan, pd.NaT, np.nan, "Nahi Hai"]
})
print(df)

# where na it drop the row row when any shell value of row is none  {it can't change the original DataFrame}
# print(df.dropna())

#  it delete row when all column value of row is Nan exp: in this datafram Row No. : 3
print()
# print(df.dropna(how='all'))

# when we want to do the same work in the column then we use axis=1
# it men it delete the column when all value of the column is none
# print(df.dropna(how='all', axis=1))

print(df.drop_duplicates(subset=['Name']))