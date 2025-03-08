import sqlite3
import os

db_path = os.path.abspath("data.db")
print(f"📌 Using database file: {db_path}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("📌 Tables found in DB:", tables)

conn.close()
