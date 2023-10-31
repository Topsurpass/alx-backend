#!/usr/bin/env python3
"""This module contains the instantiation of Babel object
in order to configure available languages in our app"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)

class Config:
    """Configure the available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

"""Configure your app from the Config class"""
app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """decorator makes fxn invoked for each request
    to select a language translation to use for that
    request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def welcome() -> str:
    """Render html page, now with languages configuration"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
