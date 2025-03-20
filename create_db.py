import sqlite3

# Connect to SQLite database (if the file doesn't exist, it will be created)
conn = sqlite3.connect('database.db')  # This creates the database file

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for places (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    image_url TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
