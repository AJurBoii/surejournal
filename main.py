from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(
    version="0.1.0",
    title="SureJournal API",
    description="A simple journaling API built with FastAPI.",
    contact={"name": "Amarius LeSure", "email": "amariusj.lesure@gmail.com"},
)

templates = Jinja2Templates(directory="templates")

entries: list[dict] = [
    {
        "user": "aj.lesure",
        "id": 0,
        "date": datetime(2026, 3, 19, 13, 4, 0).strftime("%m-%d-%Y, %I:%M %p"),
        "content": "Today I felt a little anxious to learn FastAPI, but I know everything will work out as long as I pace myself and have confidence.",
    },
    {
        "user": "aj.lesure",
        "id": 1,
        "date": datetime(2026, 3, 19, 13, 11, 0).strftime("%m-%d-%Y, %I:%M %p"),
        "content": "I just learned how to create datetime objects and format them into strings. I feel pretty good about that!",
    },
    {
        "user": "random.person",
        "id": 2,
        "date": datetime.now().strftime("%m-%d-%Y, %I:%M %p"),
        "content": "Hello, I am a random person using this journaling app to write about my feelings and keep track of my mood. It's helpful!!",
    },
]


@app.get("/", include_in_schema=False)
@app.get("/entries", include_in_schema=False)
def home():
    return "<h1>SureJournal</h1><h2>Welcome to SureJournal</h2>"


@app.get("/api/entries")
def get_entries():
    return entries
