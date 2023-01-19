import pandas as pd

# import jinja2
# from pycaret.classification import *

df11 = pd.read_excel('D:/pandas_excelFiles/11월.xlsx')
df12 = pd.read_excel('D:/pandas_excelFiles/12월.xlsx')

# print("before")
# print("11월")
# print(df11)
# print("12월")
# print(df12)

# df12.insert(6, 'total_11',df11['name'].map(df11.set_index('name')['total']))
# df12=pd.merge(df12, df11, how='outer', on=['name', 'total'], indicator=True)
df12 = pd.merge(df12, df11[['name', 'total']], on='name', how='outer')
print("after!")
print(df12)
result = []
f_result = []

# print(df12['name'][0])
for i in range(len(df12)):
    if df12['total_x'][i] == df12['total_y'][i]:
        result.append('true')
    else:
        result.append('false')
        df12.style.applymap(draw_color_cell, color='#ff9090', subset=pd.IndexSlice[i, len(df12.coulums)])
        f_result.append(i)

print(result)
df12['result'] = result
print(df12)
print(len(df12.columns))
# f_result=result.index('false')
print('f_result:', f_result)


# print('df12', len(df12))
# print('result:', len(result))

def draw_color_cell(x, color):
    color = f'background-color:{color}'
    return color
