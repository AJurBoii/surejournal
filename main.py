from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from entries import JournalEntry

app = FastAPI(
    version="0.1.0",
    title="SureJournal API",
    description="A simple journaling API built with FastAPI.",
    contact={"name": "Amarius LeSure", "email": "amariusj.lesure@gmail.com"},
)

templates = Jinja2Templates(directory="templates")

entries: list[JournalEntry] = [
    JournalEntry(
        user="aj.lesure",
        content="Today I felt a little anxious to learn FastAPI, but I know everything will work out as long as I pace myself and have confidence.",
        timestamp=datetime(2026, 3, 19, 13, 4, 0),
    ),
    JournalEntry(
        user="aj.lesure",
        content="I just learned how to create datetime objects and format them into strings. I feel pretty good about that!",
        timestamp=datetime(2026, 3, 19, 13, 11, 0),
    ),
    JournalEntry(
        user="random.person",
        content="Hello, I am a random person using this journaling app to write about my feelings and keep track of my mood. It's helpful!!",
        timestamp=datetime.now(),
    ),
]


@app.get("/", include_in_schema=False)
@app.get("/entries", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"entries": entries})


@app.get("/api/entries")
def get_entries():
    return entries
