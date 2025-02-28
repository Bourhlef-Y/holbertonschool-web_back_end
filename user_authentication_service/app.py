#!/usr/bin/env python3
"""Module de l'application Flask
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """Route GET racine qui retourne un message de bienvenue"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
