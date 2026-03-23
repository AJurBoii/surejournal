from datetime import datetime

id: int = 0  # global variable to keep track of entry IDs, incremented each time a new entry is created


class JournalEntry:
    def __init__(self, user: str, content: str, timestamp: datetime):
        global id
        self.user: str = user
        self.content: str = content
        self.id: int = id
        id += 1
        self.timestamp: list[str] = [timestamp.strftime("%m-%d-%Y, %I:%M %p")]

    def editEntry(self, content: str):
        self.content = content
        self.timestamp.append(datetime.now().strftime("%m-%d-%Y, %I:%M %p"))

    def getEntry(self) -> str:
        return self.content

    def getUser(self) -> str:
        return self.user

    def getTimestamp(self) -> str:
        return (
            "Posted "
            + self.timestamp[len(self.timestamp) - 1]
            + " (last edited "
            + self.timestamp[len(self.timestamp) - 1]
            + ")"
            if len(self.timestamp) > 1
            else "Posted " + self.timestamp[0]
        )


testEntry = JournalEntry("aj.lesure", "This is a test entry.", datetime.now())
print(testEntry.getEntry())
print(testEntry.getUser())
print(testEntry.getTimestamp())
testEntry.editEntry("The content of the entry has changed.")
print(testEntry.getTimestamp())
