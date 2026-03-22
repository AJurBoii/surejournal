from datetime import datetime


class JournalEntry:
    def __init__(self, user: str, content: str):
        self.user = user
        self.content = content
        self.timestamp = [datetime.now().strftime("%m-%d-%Y, %I:%M %p")]

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


testEntry = JournalEntry("aj.lesure", "This is a test entry.")
print(testEntry.getEntry())
print(testEntry.getUser())
print(testEntry.getTimestamp())
testEntry.editEntry("The content of the entry has changed.")
print(testEntry.getTimestamp())
