# HTML Generator with FastAPI

## Features
- Uses FastAPI to serve a dynamically generated HTML page.
- Stores API keys and channel IDs in `data.json`.
- Automatically replaces placeholders in `template.html`.

## Setup
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:  
   ```bash
   uvicorn main:app --reload
   ```

3. Visit `http://127.0.0.1:8000/` to see your generated page.
