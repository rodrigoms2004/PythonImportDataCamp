# https://www.prio.org/Data/Armed-Conflict/Battle-Deaths/The-Battle-Deaths-Dataset-version-30/

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = './OtherFiles/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())


# Parse the first sheet and rename the columns: df1
df3 = xl.parse(0, skiprows=[1], names=['Country', 'AAM due to War (2002)'])

# # Print the head of the DataFrame df1
print(df3.head())

# # Parse the first column of the second sheet and rename the column: df2
df4 = xl.parse(1, parse_cols=[0], skiprows=[1], names=['Country'])

# # Print the head of the DataFrame df2
print(df4.head())
