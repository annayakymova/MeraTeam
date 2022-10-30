from app import app
from flask import render_template


@app.route('/')
def hello():
    return "Hello user"


@app.route("/calc/<int:num1>/<int:num2>")
def calc(num1, num2):
    return render_template("index.html", summa=f'{num1} + {num2} = {num1 + num2}')

