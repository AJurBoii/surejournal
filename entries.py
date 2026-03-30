import time
from datetime import datetime


class JournalEntry:
    def __init__(self, content: str, timestamp: datetime):
        self.content: str = content
        self.timestamp: list[str] = [timestamp.strftime("%m-%d-%Y, %I:%M %p")]

    def editEntry(self, content: str):
        self.content = content
        self.timestamp.append(datetime.now().strftime("%m-%d-%Y, %I:%M %p"))

    def getContent(self) -> str:
        return self.content

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


class UserJournal:
    def __init__(self, user: str):
        self.id: int = 0
        self.user: str = user
        self.entries: dict[int, JournalEntry] = {}

    def getUser(self) -> str:
        return self.user

    def getEntries(self) -> dict[int, JournalEntry]:
        return self.entries

    def addEntry(self, content: str) -> None:
        self.entries[self.id] = JournalEntry(content, datetime.now())
        self.id += 1

    def __repr__(self):
        text = ["User: " + self.user]
        for key in self.entries:
            text.append(f"\tEntry ID: {key}\n\t{self.entries[key]}")
        return "\n".join(text)


testJournal = UserJournal("aj.lesure")
testJournal.addEntry("This is a test entry")
testJournal.addEntry("This is a second test entry")

secondTestJournal = UserJournal("random.person")
secondTestJournal.addEntry("This is the first entry of another user.")
secondTestJournal.addEntry("This is the second entry of anonther user.")
secondTestJournal.addEntry("This is the third entry of another user.")

print(testJournal)
print(secondTestJournal)
# print(testEntry.getEntry())
# print(testEntry.getUser())
# print(testEntry.getTimestamp())
# testEntry.editEntry("The content of the entry has changed.")
# print(testEntry.getTimestamp())
