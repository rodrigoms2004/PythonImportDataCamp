import pandas as pd

file = './OtherFiles/urbanpop.xlsx'

data = pd.ExcelFile(file)

print(data.sheet_names) # ['1960-1966', '1967-1974', '1975-2011']

df1 = data.parse('1960-1966')   # sheet name, as a string
df2 = data.parse(0)             # sheet index, as a float

