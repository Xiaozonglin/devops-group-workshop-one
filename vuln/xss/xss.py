import flask

app = flask.Flask(__name__)

@app.get("/")
def index():
    # directly use input from user without sanitization
    return str(flask.request.args.get("html")), 200

if __name__ == "__main__":
    app.run()