from datetime import datetime


def create_entry(user: str, content: str) -> dict:
    entry = {"user": user, "datetime": datetime.now().strftime("%m/%d/%Y, %I:%M %p")}
    return entry
