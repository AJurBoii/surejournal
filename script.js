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

function saveEntry(entryText) {
    // Initializes the transaction in which we'll be adding an object. The two parameters establish the scope of the transaction (which stores, possibly multiple, can be interacted with) and the access type.
    const transaction = db.transaction("entries", "readwrite");
    // Specifies which specific store we'll be interacting with within this transaction
    const store = transaction.objectStore("entries");

    // We must initialize an object to add to the db, otherwise a the auto-generated id instance variable can't be added and thus no key path.
    entry = {
        text: entryText,
        timestamp: new Date().toLocaleString()
    }

    // The main request that allows us to interact with the DB within this transaction
    const request = store.add(entry);

    // request callback
    request.onsuccess = () => {
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

            referenceElement.insertAdjacentElement('afterend', newElement);
        })
    }
}

const saveBtn = document.getElementById("save");


saveBtn.addEventListener("click", () => {
    const entryText = document.getElementById("entry").value;
    saveEntry(entryText);
    location.reload();
});