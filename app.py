from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return '<h1>hello!</h1>'

@app.route('/settings')
def settings():
    return '<h1>Settings</h1>'
