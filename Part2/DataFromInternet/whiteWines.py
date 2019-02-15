import pandas as pd
from urllib.request import urlretrieve

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

urlretrieve(url, './Part2/DataFromInternet/winequality-white.csv')

df = pd.read_csv('./Part2/DataFromInternet/winequality-white.csv', sep=';')
print(df.head())
