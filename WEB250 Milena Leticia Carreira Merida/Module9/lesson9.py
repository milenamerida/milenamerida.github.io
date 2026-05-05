from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = "pizza.db"

FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Pizza Orders</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>

<body>
<h1>Pizza Ordering System</h1>

<form method="POST">
    <p>Name: <input type="text" name="name" required></p>
    <p>Pizza Type:
        <select name="pizza">
            <option>Cheese</option>
            <option>Pepperoni</option>
            <option>Veggie</option>
        </select>
    </p>
    <p>Quantity: <input type="number" name="quantity" required></p>

    <input type="submit" value="Place Order">
</form>

<hr>
"""

@app.route("/", methods=["GET"])
def home():
    check_database()
    return FORM + show_orders() + "</body></html>"

@app.route("/", methods=["POST"])
def order():
    name = request.form["name"]
    pizza = request.form["pizza"]
    quantity = int(request.form["quantity"])

    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        # customer
        cursor.execute(
            "INSERT INTO Customers(name) VALUES(?)",
            (name,)
        )
        customer_id = cursor.lastrowid

        # order
        cursor.execute(
            "INSERT INTO Orders(customer_id, date) VALUES(?, datetime('now'))",
            (customer_id,)
        )
        order_id = cursor.lastrowid

        # details
        cursor.execute(
            "INSERT INTO OrderDetails(order_id, pizza_type, quantity) VALUES(?, ?, ?)",
            (order_id, pizza, quantity)
        )

        connection.commit()

    return FORM + show_orders() + "</body></html>"

def check_database():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            date TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS OrderDetails(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            pizza_type TEXT,
            quantity INTEGER
        );
        """)

def show_orders():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT Customers.name, Orders.id, Orders.date, OrderDetails.pizza_type, OrderDetails.quantity
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.id
        JOIN OrderDetails ON Orders.id = OrderDetails.order_id
        ORDER BY Orders.id DESC
        """)

        rows = cursor.fetchall()

        result = "<h2>All Orders</h2>"
        result += "<table>"
        result += "<tr><th>Name</th><th>Order ID</th><th>Date</th><th>Pizza</th><th>QYT</th></tr>"

        for row in rows:
            result += f"<tr><td>{row[0]}</td>"
            result += f"<td>{row[1]}</td>"
            result += f"<td>{row[2]}</td>"
            result += f"<td>{row[3]}</td>"
            result += f"<td>{row[4]}</td></tr>"

        result += "</table>"

        return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
