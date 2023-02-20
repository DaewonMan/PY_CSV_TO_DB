import csv
import sqlite3

# Open the CSV file
with open('data.csv', 'r') as f:
    # Create a csv reader object
    reader = csv.reader(f)
    # Get the column headers from the first row of the CSV file
    headers = next(reader)
    
    # Open a connection to the SQLite database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    
    # Create a new table in the database with the same column names as the CSV file
    # c.execute(f"CREATE TABLE IF NOT EXISTS mytable ({','.join(headers)})")
    
    # Insert the data from the CSV file into the database
    for row in reader:
        c.execute(f"INSERT INTO mytable ({','.join(headers)}) VALUES ({','.join('?' * len(headers))})", row)
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()