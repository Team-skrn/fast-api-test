from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

@app.get("/")
def home(request: Request):
    data = load_data()
    return templates.TemplateResponse("template.html", {"request": request, **data})
