import ribbitxdb as sqlite3
from flask import Flask, request, render_template, g

app = Flask(__name__)
DATABASE = "sqli.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute("DROP TABLE IF EXISTS users;")
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
    db.execute("INSERT INTO users (username, password) VALUES ('alice', 'alice123');")
    db.execute("INSERT INTO users (username, password) VALUES ('bob', 'bob456');")
    db.commit()
    db.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # alice' --

    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    row = get_db().execute(sql).fetchone()

    if row:
        return f"登录成功,欢迎 {row[1]}"
    return "用户名或密码错误", 401

if __name__ == "__main__":
    init_db()
    app.run(debug=True)