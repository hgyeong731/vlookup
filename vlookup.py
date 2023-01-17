import pandas as pd

df11=pd.read_excel('D:/pandas_excelFiles/11월.xlsx')
df12=pd.read_excel('D:/pandas_excelFiles/12월.xlsx')

print("before")
print("11월")
print(df11)
print("12월")
print(df12)

# df12.insert(6, 'total_11',df11['name'].map(df11.set_index('name')['total']))
# df12=pd.merge(df12, df11, how='outer', on=['name', 'total'], indicator=True)
df12=pd.merge(df12, df11[['name', 'total']], on='name', how='outer')
print("after")
print(df12)