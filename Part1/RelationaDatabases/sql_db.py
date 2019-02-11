# SQLAlquemy
#     Works with many Relational Database Management Systems

from sqlalchemy import create_engine

# db_file = './RelationaDatabases/Northwind_large.sqlite/Northwind_large.sqlite'
db_file = './RelationaDatabases/Northwind_small.sqlite'
engine = create_engine('sqlite:///' + db_file)

table_names = engine.table_names()

print(table_names)  # ['Category', 'Customer', 'CustomerCustomerDemo', ...]

import pandas as pd

query = "SELECT * FROM OrderDetail"

with engine.connect() as con:
    rs = con.execute(query)
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()

print(df.head())

# con = engine.connect()
# rs = con.execute(query)

# df = pd.DataFrame(rs.fetchall())
# df.columns = rs.keys()

# con.close()
# print(df.head())