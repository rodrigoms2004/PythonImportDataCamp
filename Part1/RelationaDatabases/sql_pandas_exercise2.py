# Import packages
from sqlalchemy import create_engine
import pandas as pd

# db_file = './RelationaDatabases/Northwind_small.sqlite'
db_file = './RelationaDatabases/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + db_file)

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)

# Print head of DataFrame
print(df.head())