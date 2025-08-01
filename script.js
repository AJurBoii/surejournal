let db;

const request = indexedDB.open("JournalDB", 1);

request.onupgradeneeded = (event) => {
    db = event.target.result;
    const store = db.createObjectStore("entries", { keyPath: "id", autoIncrement: true });
}

request.onsuccess = (event) => {
    db = event.target.result;
    loadEntries();
}

request.onerror = (event) => {
    console.log("indexedDB error: " + event.target.error);
}

function saveEntry(entryText, entryMood) {
    // Initializes the transaction in which we'll be adding an object. The two parameters establish the scope of the transaction (which stores, possibly multiple, can be interacted with) and the access type.
    const transaction = db.transaction("entries", "readwrite");
    // Specifies which specific store we'll be interacting with within this transaction
    const store = transaction.objectStore("entries");

    // We must initialize an object to add to the db, otherwise a the auto-generated id instance variable can't be added and thus no key path.
    entry = {
        text: entryText,
        mood: entryMood,
        timestamp: new Date().toLocaleString()
    }

    // The main request that allows us to interact with the DB within this transaction
    const request = store.add(entry);

    // request callback
    request.onsuccess = () => {
        alert("Entry saved!");
        console.log("Entry saved!");
    }

}

function loadEntries() {
    const transaction = db.transaction("entries", "readonly");
    const store = transaction.objectStore("entries");
    const request = store.getAll();

    entriesList = document.getElementById("entriesList");

    const referenceElement = document.getElementById("startOfList");

    request.onsuccess = (event) => {
        entries = event.target.result;
        // load each entry newest first
        entries.forEach(entry => {
            newElement = document.createElement('p');
            newElement.innerHTML = `<strong>${entry.timestamp}</strong>: ${entry.text}`;
            if (entry.mood) {
                newElement.innerHTML += ` | Mood: ${entry.mood}`;
            }
            deleteButton = document.createElement('button');
            deleteButton.innerHTML = `Delete`;
            deleteButton.addEventListener("click", () => {
                deleteEntry(entry.id);
            });

            referenceElement.insertAdjacentElement('afterend', deleteButton);
            referenceElement.insertAdjacentElement('afterend', newElement);
        })
    }
}

function deleteEntry(entryID) {
    const transaction = db.transaction("entries", "readwrite");
    const store = transaction.objectStore("entries");
    const request = store.delete(entryID);

    request.onsuccess = () => {
        alert("Entry deleted.");
        location.reload();
    }
}

const saveBtn = document.getElementById("save");

saveBtn.addEventListener("click", () => {
    const moodForm = document.getElementById("moodForm");
    const entryMood = moodForm.elements['mood'].value;

    if (entryMood == "") {
        console.log("No mood selected.");
    } else {
        console.log("Mood: " + entryMood);
    }

    const entryText = document.getElementById("entry").value;
    saveEntry(entryText, entryMood);
    location.reload();
});