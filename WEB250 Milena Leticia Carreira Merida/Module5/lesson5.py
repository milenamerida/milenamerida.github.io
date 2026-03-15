from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/earthquake", methods=["GET","POST"])
def earthquake():
    results = []

    if request.method == "POST":
        file = request.files["file"]

        if file:
            text = file.read().decode()
            lines = text.strip().split("\n")
            for line in lines:
                date, name, magnitude = line.split(",")
                magnitude = float(magnitude)
                description = get_description(magnitude)

                results.append({
                    "date": date,
                    "name": name,
                    "magnitude": magnitude,
                    "description": description
                })

    return render_template("earthquake.html", results = results)

def get_description(magnitude):
    if magnitude < 5:
        return "Small"
    elif magnitude < 7:
        return "Moderate"
    elif magnitude < 8:
        return "Major"
    elif magnitude < 10:
        return "Great"
    else:
        return "Super"
           

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
