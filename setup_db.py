import sqlite3

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create the 'pages' table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS pages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    api_key TEXT NOT NULL,
    channel_id TEXT NOT NULL
)
""")

# Insert sample data (Run this only once)
cursor.execute("INSERT INTO pages (title, api_key, channel_id) VALUES (?, ?, ?)", 
               ("Pampa Sump", "9VMWLF58YXMSKZ4O", "2322174"))

conn.commit()
conn.close()

print("Database setup complete!")
