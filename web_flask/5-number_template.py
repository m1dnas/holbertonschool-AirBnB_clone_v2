#!/usr/bin/python3
"""aaaa"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    return("HBNB")


@app.route('/c/<text>')
def c(text=None):
    return "C " + str(text).replace("_", " ")


@app.route('/python/<text>')
@app.route('/python')
def python(text="is cool"):
    return "Python " + str(text).replace("_", " ")


@app.route('/number/<int:n>')
def is_this_pinga_a_number(n):
    return n + " is a number"


@app.route('/number_template/<int:n>')
def temporalmente_tarde(n):
    return render_template("5-number.html", var=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
