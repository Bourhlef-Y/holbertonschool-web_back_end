#!/usr/bin/env python3
"""Basic Flask app module"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders the index page
    Returns:
        str: Rendered template for index page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
