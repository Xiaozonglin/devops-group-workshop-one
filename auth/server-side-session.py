from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/set/')
def set():
    session['key'] = 'admin'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

if __name__ == "__main__":
    app.run()