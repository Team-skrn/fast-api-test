import sqlite3
from jinja2 import Template

# Connect to SQLite database (or replace with your actual DB)
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Fetch title and other variables
cursor.execute("SELECT title, api_key, channel_id FROM pages LIMIT 1")  # Modify query as needed
row = cursor.fetchone()
conn.close()

if row:
    title, api_key, channel_id = row
else:
    title, api_key, channel_id = "DefaultTitle", "DEFAULT_API_KEY", "DEFAULT_CHANNEL_ID"

# Load the base HTML template
with open("templates/template.html", "r") as file:
    template_content = file.read()

# Use Jinja2 to replace variables
template = Template(template_content)
rendered_html = template.render(title=title, api_key=api_key, channel_id=channel_id)

# Generate the filename based on the title
filename = f"{title.replace(' ', '_').lower()}.html"

# Save the generated HTML file
with open(filename, "w") as file:
    file.write(rendered_html)

print(f"Generated HTML file: {filename}")
