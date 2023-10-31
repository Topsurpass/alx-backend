#!/usr/bin/env python3
"""This module contains the instantiation of Babel object
in order to configure available languages in our app"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configure the available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""Configure your app using the Config class"""
app.config.from_object(Config)


@app.route('/')
def welcomeConf() -> str:
    """Render html page, now with languages configuration"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
