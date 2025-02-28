#!/usr/bin/env python3
"""Module de l'application Flask.

Ce module implémente une API REST pour l'authentification des utilisateurs.
Il fournit des routes pour l'enregistrement, la connexion et la gestion
des sessions utilisateur.
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome() -> str:
    """Route GET racine qui retourne un message de bienvenue.

    Returns:
        str: JSON contenant le message de bienvenue
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Route POST pour enregistrer un nouvel utilisateur.

    Returns:
        str: JSON avec le statut de l'opération
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """Route POST pour la connexion d'un utilisateur.

    Returns:
        str: JSON avec le statut de la connexion
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(
        jsonify({"email": email, "message": "logged in"})
    )
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """Route DELETE pour déconnecter un utilisateur.

    Returns:
        str: Redirection vers la page d'accueil
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """Route GET pour obtenir le profil de l'utilisateur.

    Returns:
        str: JSON contenant l'email de l'utilisateur
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """Route POST pour obtenir un token de réinitialisation de mot de passe.

    Returns:
        str: JSON contenant l'email et le token de réinitialisation
    """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({
            "email": email,
            "reset_token": reset_token
        })
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
