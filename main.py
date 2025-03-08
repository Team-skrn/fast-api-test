import os
import sqlite3

# Ensure the database file is in the correct location
db_path = os.path.join(os.getcwd(), "data.db")
print(f"📌 Using database file: {db_path}")  # Print the database path

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Debug: Check if the table actually exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("📌 Tables in database:", tables)

# Check if 'pages' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pages';")
result = cursor.fetchone()

if result:
    print("✅ Table 'pages' exists! Proceeding with query.")
else:
    print("❌ Table 'pages' does NOT exist! Database setup failed.")

conn.close()
