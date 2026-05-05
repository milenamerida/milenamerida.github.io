import os
import flask
import bcrypt

app = flask.Flask(__name__)
app.secret_key = os.urandom(32)

users = [
    {
        "userid": 1,
        "username": "admin",
        "password": bcrypt.hashpw(b"admin", bcrypt.gensalt()),
        "role": "employee"
    },
    {
        "userid": 2,
        "username": "manager",
        "password": bcrypt.hashpw(b"manager", bcrypt.gensalt()),
        "role": "manager"
    }
]

@app.route("/")
def home():
    username = flask.request.cookies.get("username")
    userid = flask.session.get("userid")

    return flask.render_template(
        "index.html",
        username=username,
        logged_in=bool(userid)
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return render_login()

    username = flask.request.form["username"]
    password = flask.request.form["password"]

    user = authenticate(username, password)

    if user:
        flask.session["userid"] = user["userid"]
        flask.session["role"] = user["role"]

        resp = flask.redirect("/dashboard")
        resp.set_cookie("username", username)
        return resp

    return "Login failed. <a href='/login'>Try Again</a>"

@app.route("/dahsboard")
def dashboard():
    if "userid" not in flask.session:
        return flask.redirect("/login")

    role = flask.session.get("role")

    return f"""
    <h1>Dashboard</h1>
    <p>Logged in as: {role}</p>
    <a href="/logout">Logout</a>

    """

@app.route("/logout")
def logout():
    flask.session.clear()
    resp = flask.redirect("/")
    resp.set_cookie("username", "", max_age=0)
    return resp

def authenticate(username, password):
    for user in users:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode(), user["password"]):
                return user

    return None

def render_login():
    return """
    <h1>Login</h1>

    <form method="POST">
        <p>Username: <input name="username"></p>
        <p>Password: <input type="password" name="password"></p>
        <button type="submit">Login</button>
    </form>

    """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
