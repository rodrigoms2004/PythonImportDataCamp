# Import packages
from sqlalchemy import create_engine
import pandas as pd

# db_file = './RelationaDatabases/Northwind_small.sqlite'
db_file = './RelationaDatabases/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + db_file)

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000", engine)

# Print head of DataFrame
print(df.head())