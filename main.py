Run python main.py  # This should generate an HTML file in the repo
Traceback (most recent call last):
  File "/home/runner/work/fast-api-test/fast-api-test/main.py", line 9, in <module>
    cursor.execute("SELECT title, api_key, channel_id FROM pages LIMIT 1")  # Modify query as needed
sqlite3.OperationalError: no such table: pages
