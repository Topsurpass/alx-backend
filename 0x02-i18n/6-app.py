#!/usr/bin/env python3

"""This module contains the instantiation of Babel object
in order to configure available languages in our app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configure the available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""Configure your app from the Config class"""
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieve a user from database if login_as is passed
    to the request URL and the ID can be found, else none"""

    user_id = request.args.get('login_as')
    if user_id:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """Execute before all other function.
    Set output of the get_user method as global"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Retrieve client preferred locale from the locale query parameter
    in the request URL"""
    # Locale from URL parameters
    preferred_locale = request.args.get('locale')
    if preferred_locale in app.config['LANGUAGES']:
        return preferred_locale
    # Locale from user setting
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    # Locale from http request header
    http_req_header_locale = request.headers.get('locale', '')
    if http_req_header_locale in app.config['LANGUAGES']:
        return http_req_header_locale
    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome() -> str:
    """Render html page, now with languages configuration"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
