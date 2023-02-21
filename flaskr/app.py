from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def test():
    return render_template("calculator.html")


def addNumber(value:str):
    digit = value