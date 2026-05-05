const API = "/records";

async function loadRecords() {
    const res = await fetch(API);
    const data = await res.json();

    const table = document.querySelector("#table tbody");
    table.innerHTML = "";

    data.forEach(r => {
        table.innerHTML += `
            <tr>
                <td>${r.id}</td>
                <td>${r.text}</td>
                <td>${r.number}</td>
                <td>${r.date}</td>
            </tr>
        `;
    });
}

async function createRecord() {
    await fetch(API, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            text: document.getElementById("text").value,
            number: parseFloat(document.getElementById("number").value),
            date: document.getElementById("date").value
        })
    });

    loadRecords();
}

async function updateRecord() {
    const id = document.getElementById("updateId").value;
    
    await fetch(`${API}/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            text: document.getElementById("updateText").value,
            number: parseFloat(document.getElementById("updateNumber").value),
            date: document.getElementById("updateDate").value
        })
    });

    loadRecords();
}

async function deleteRecord() {
    const id = document.getElementById("deleteId").value;

    await fetch(`${API}/${id}`, {
        method: "DELETE"
    });

    loadRecords();
}

loadRecords();