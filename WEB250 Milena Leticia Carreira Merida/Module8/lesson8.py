from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/storm8")
def storm8():
    try:
        data = get_data()
        records = get_records(data)

        records.sort(key=lambda x: x["kmh"], reverse=True)

        return render_template("storm8.html", records=records)

    except Exception as e:
        return str(e)

def get_data():
    with open("storm.json") as f:
        return json.load(f)

def get_records(data):
    records = []

    for item in data:
        try:
            date = item["Date"]
            name = item["Storm"]
            wind = item["MaximumSustainedWinds"]

            index = wind.find(" km/h")
            kmh = float(wind[:index])
            mph = kmh * 0.621371

            category = get_category(kmh)

            record = {
                "date": date,
                "name": name,
                "kmh": kmh,
                "mph": mph,
                "category": category
            }

            records.append(record)

        except:
            continue

    return records

def get_category(kmh):
    if kmh < 119:
        return "Tropical_Storm"
    elif kmh < 154:
        return "Category_1"
    elif kmh < 178:
        return "Category_2"
    elif kmh < 209:
        return "Category_3"
    elif kmh < 252:
        return "Category_4"
    else:
        return "Category_5"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
