# Import packages
from sqlalchemy import create_engine
import pandas as pd

db_file = './RelationaDatabases/Northwind_small.sqlite'
# db_file = './RelationaDatabases/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + db_file)

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT OrderId, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID", engine)

# Print head of DataFrame
print(df.head())
