#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def holinga():
    """aaaa"""
    return("Hello HBNB!")

app.run(host="0.0.0.0")