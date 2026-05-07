from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "dog.db"

def check_database():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Dogs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            breed TEXT,
            age INTEGER,
            weight REAL
        );
        """)

@app.route("/")
def home():
    check_database()
    return render_template("index.html")

# add dog
@app.route("/add", methods=["GET", "POST"])
def add_dog():
    if request.method == "POST":
        name = request.form["name"]
        breed = request.form["breed"]
        age = request.form["age"]
        weight = request.form["weight"]

        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Dogs (name, breed, age, weight) VALUES (?,?,?,?)",
                           (name, breed, age, weight)
            )
            connection.commit()

    return render_template("add.html")

# view dogs
@app.route("/view")
def view_dogs():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Dogs ORDER BY id DESC")
        dogs = cursor.fetchall()

    return render_template("view.html", dogs=dogs)

# find dog
@app.route("/find", methods=["GET", "POST"])
def find_dog():
    result = None

    if request.method == "POST":
        search_name = request.form["name"]

        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Dogs WHERE name = ?", (search_name,))
            dog = cursor.fetchone()

        if dog:
            result = f"Dog found: {dog[1]} ({dog[2]})"
        else:
            result = "Dog not found"

    return render_template("find.html", result=result)

@app.route("/quit")
def quit_program():
    return render_template("quit.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
            
    
        
