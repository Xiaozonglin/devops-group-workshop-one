from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "change-me" # weak secret key

@app.route("/")
def index():
    if "username" in session:
        return f"""
        <h1>欢迎回来，{session["username"]}！</h1>
        """
    return "<h1>请登录</h1>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        if username:
            session["username"] = username
            return redirect(url_for("index"))

    return """
    <form method="post">
        <input type="text" name="username">
        <input type="submit" value="登录">
    </form>
    """