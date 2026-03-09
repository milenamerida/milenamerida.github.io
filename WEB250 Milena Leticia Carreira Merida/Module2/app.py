from flask import Flask, render_template
import datetime
import socket
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/server")
def server_info():
    current_time = datetime.datetime.now()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = platform.system() + " " + platform.release()
    python_version = platform.python_version()

    return render_template(
        "server_info.html",
        time = current_time,
        hostname = hostname,
        ip = ip_address,
        os = os_info,
        python = python_version
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
