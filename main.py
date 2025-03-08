import os
import sqlite3

# Get the correct path dynamically
db_path = os.path.join(os.getcwd(), "database", "data.db")

print(f"📌 Using database file: {db_path}")

if not os.path.exists(db_path):
    print("❌ ERROR: data.db is missing!")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("📌 Tables found in DB:", cursor.fetchall())

conn.close()
