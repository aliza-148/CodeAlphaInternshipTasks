"""
Sample Flask application used as the audit target for Task 3.
Intentionally contains common vulnerability patterns for review purposes.
"""
import sqlite3
import os
import subprocess
import pickle
from flask import Flask, request, redirect, make_response

app = Flask(__name__)
app.secret_key = "supersecret123"  # hardcoded secret

DB_PATH = "users.db"


def get_db():
    return sqlite3.connect(DB_PATH)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    conn = get_db()
    cur = conn.cursor()
    # SQL Injection: user input concatenated directly into query
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cur.execute(query)
    user = cur.fetchone()
    if user:
        resp = make_response(redirect("/dashboard"))
        resp.set_cookie("session", str(user[0]))
        return resp
    return "Invalid credentials", 401


@app.route("/search")
def search():
    term = request.args.get("q", "")
    # Reflected XSS: unsanitized input echoed back into HTML
    return f"<h1>Results for {term}</h1>"


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # Command Injection: user input passed to shell
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return output


@app.route("/load")
def load():
    data = request.args.get("data")
    # Insecure Deserialization
    obj = pickle.loads(bytes.fromhex(data))
    return str(obj)


@app.route("/file")
def read_file():
    filename = request.args.get("name")
    # Path Traversal: no sanitization of filename
    path = os.path.join("/var/app/uploads", filename)
    with open(path, "r") as f:
        return f.read()


@app.route("/admin")
def admin():
    # Broken Access Control: no auth check at all
    return "Welcome to the admin panel"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # debug mode + bind-all in "production"
