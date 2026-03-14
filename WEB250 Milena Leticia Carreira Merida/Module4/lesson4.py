from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/average", methods=["GET","POST"])
def average():
    total = 0
    count = 0
    average = None

    if request.method == "POST":
        value = request.form["value"]
        total = float(request.form["total"])
        count = int(request.form["count"])

        if value == "":
            total = 0
            count = 0
        else:
            value = float(value)
            total += value
            count += 1
            average = total/count

    return render_template(
        "average.html",
        total = total,
        count = count,
        average = average
    )
           

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
