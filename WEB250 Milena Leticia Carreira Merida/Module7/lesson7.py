from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/storm7", methods=["GET","POST"])
def storm7():
    table = []

    if request.method == "POST":
        file = request.files["file"]

        if file:
            text = file.read().decode()
            lines = text.strip().split("\n")

            if "date" in lines[0].lower():
                lines.pop(0)
            for line in lines:
                try:
                    record = process_line(line)
                    table.append(record)
                except ValueError as e:
                    return str(e)
                
            table.sort(key=lambda x: x["kmh"], reverse=True)

    return render_template("storm7.html", table=table)

def process_line(line):
    parts = line.split(",")

    if len(parts) != 3:
        raise ValueError("Invalid CSV format")

    date = parts[0]
    name = parts[1]

    try:
        kmh = float(parts[2])
    except:
        raise ValueError("Invalid wind value")

    mph = kmh * 0.621371
    category = get_category(kmh)

    record = {
        "date": date,
        "name": name,
        "kmh": kmh,
        "mph": mph,
        "category": category
    }
    
    return record

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
