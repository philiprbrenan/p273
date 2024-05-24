import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Create engine and metadata
engine = create_engine('postgresql+psycopg2://myuser:mypassword@localhost/mydb')
metadata = MetaData()

# Define a sample table
sample_table = Table('sample', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

# Create the table
metadata.create_all(engine)

# Insert sample data
with engine.connect() as connection:
    connection.execute(sample_table.insert(), [
        {'name': 'Alice'},
        {'name': 'Bob'}
    ])

    # Execute a select statement
    result = connection.execute(sample_table.select())
    for row in result:
        print(row)
