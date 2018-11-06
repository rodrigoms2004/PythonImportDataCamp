
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
db_file = './RelationaDatabases/Northwind_small.sqlite'
engine = create_engine('sqlite:///' + db_file)

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE Id >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())