from flask import Flask, render_template, request
import datetime
import socket
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/converter", methods=["GET","POST"])
def converter():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        i_unit = request.form["i_unit"]
        f_unit = request.form["f_unit"]

        if i_unit == "km":
            meters = value * 1000
        elif i_unit == "cm":
            meters = value/100
        else:
            meters = value

        if f_unit == "km":
            result = meters/1000
        elif f_unit == "cm":
            result = meters * 100
        else:
            result = meters

    return render_template("converter.html", result=result)

@app.route("/area", methods=["GET","POST"])
def area():
    result = None
    if request.method == "POST":
        shape = request.form["shape"]
        if shape == "rectangle":
            length = float(request.form["length"])
            width = float(request.form["width"])
            result = length * width
        elif shape == "circle":
            radius = float(request.form["radius"])
            result = 3.1415 * radius * radius
        elif shape == "triangle":
            base = float(request.form["base"])
            height = float(request.form["height"])
            result = 0.5 * base * height
            
    return render_template("area.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
