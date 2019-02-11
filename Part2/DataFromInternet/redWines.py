# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, './Part2/DataFromInternet/winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('./Part2/DataFromInternet/winequality-red.csv', sep=';')
print(df.head())
