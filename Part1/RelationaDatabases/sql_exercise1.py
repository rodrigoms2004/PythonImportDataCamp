# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

db_file = './RelationaDatabases/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + db_file)

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())