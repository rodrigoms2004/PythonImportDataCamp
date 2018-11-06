# Import packages
from sqlalchemy import create_engine
import pandas as pd

# db_file = './RelationaDatabases/Northwind_small.sqlite'
db_file = './RelationaDatabases/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + db_file)

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())