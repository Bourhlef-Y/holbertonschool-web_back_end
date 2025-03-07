#!/usr/bin/env python3
"""Flask app module with Babel configuration and translations"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> str:
    """
    Determine the best match with supported languages
    Returns:
        str: Best matched language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Renders the index page with translations
    Returns:
        str: Rendered template for index page
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
