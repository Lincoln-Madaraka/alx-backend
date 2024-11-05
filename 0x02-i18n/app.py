#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel, format_datetime
from typing import Union
import pytz
import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Select and return best language match based on supported languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    user = g.get('user')
    if user:
        locale = user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    '''return the best match for timezone'''
    try:
        timezone = request.args.get('timezone')
        if timezone:
            return pytz.timezone(timezone).zone

        user = g.get('user')
        if user:
            timezone = user.get('timezone')
            return pytz.timezone(timezone).zone
        return 'UTC'
    except pytz.exceptions.UnknownTimeZoneError:
        return 'UTC'


def get_user() -> Union[object, None]:
    '''return a user if found in users or none'''
    user = request.args.get('login_as')
    if user and int(user) in users:
        return users[int(user)]
    return None


@app.before_request
def before_request() -> None:
    '''find a user and assign it to global'''
    user = get_user()
    if user:
        g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('index.html', now=datetime.datetime.now, format_datetime=format_datetime)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)