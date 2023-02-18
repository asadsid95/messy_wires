from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return '<h1>hello!</h1>'

@app.route('/users/<string:username>')
def settings(username):
    return f'<h1>{username}</h1>'
