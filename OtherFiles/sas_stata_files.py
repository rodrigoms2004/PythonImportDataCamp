import pandas as pd

# pip install sas7bdat
from sas7bdat import SAS7BDAT

with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_frame()

# importing Stata files
data = pd.read_stata('urbanpop.dta')