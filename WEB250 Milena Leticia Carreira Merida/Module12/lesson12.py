from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Record(BaseModel):
    id: int | None = None
    text: str
    number: float
    date: str | None = None

records = []
last_id = 0

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html") as f:
        return f.read()

@app.get("/records")
def get_records():
    return records

@app.post("/records")
def create_record(record: Record):
    global last_id
    last_id += 1

    new_record = {
        "id": last_id,
        "text": record.text,
        "number": record.number,
        "date": record.date if record.date else str(datetime.now())
    }

    records.append(new_record)
    return new_record

@app.put("/records/{record_id}")
def update_record(record_id: int, record: Record):
    for r in records:
        if r["id"] == record_id:
            r["text"] = record.text
            r["number"] = record.number
            r["date"] = record.date
            return r

    raise HTTPException(status_code=404, detail="Record not found.")

@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    for i in range(len(records)):
        if records [i]["id"] == record_id:
            return records.pop(i)

    raise HTTPException(status_code=404, detail="Record not found.")
