#!/usr/bin/env python3
"""This module contains basic flask server setup with
/ route and an index.html template"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def welcome() -> str:
    """Render html that display welcome message"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
