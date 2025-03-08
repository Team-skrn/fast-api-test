import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Check if 'pages' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pages';")
result = cursor.fetchone()

if result:
    print("✅ Table 'pages' exists!")
else:
    print("❌ Table 'pages' does NOT exist! Database setup failed.")

conn.close()
