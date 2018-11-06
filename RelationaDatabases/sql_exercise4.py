
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
db_file = './RelationaDatabases/Northwind_small.sqlite'
engine = create_engine('sqlite:///' + db_file)

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())