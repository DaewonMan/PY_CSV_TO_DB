import pandas as pd
import sqlite3

# Set the path to your CSV file
csv_file = 'path/to/your/csv/file.csv'

# Set the name of your SQLite database and the name of the table you want to create
db_name = 'my_database.db'
table_name = 'my_table'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Open a connection to the SQLite database and create a new table
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Get a list of the column names and data types from the DataFrame
columns = list(df.columns)
data_types = [type(df[col].values[0]).__name__ for col in columns]

# Create a table in the database with the same columns and data types as the DataFrame
table_schema = ','.join([f'{col} {data_types[i]}' for i, col in enumerate(columns)])
c.execute(f"CREATE TABLE {table_name} ({table_schema})")

# Insert the data from the DataFrame into the new table
for index, row in df.iterrows():
    values = ','.join([f"'{str(value)}'" for value in row])
    c.execute(f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({values})")

# Commit the changes and close the database connection
conn.commit()
conn.close()