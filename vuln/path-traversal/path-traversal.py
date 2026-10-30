from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/download?file=hello.txt">下载 hello.txt</a>'

@app.route("/download")
def download():
    filename = request.args.get("file", "")
    return send_file(f"files/{filename}")

"""from flask import send_from_directory
@app.route("/download")
def download():
    filename = request.args.get("file", "")
    return send_from_directory("files", filename)"""

if __name__ == "__main__":
    app.run(debug=True)