from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

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


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/api/entries")
def get_entries():
    return entries
