#!/usr/bin/env python3
"""Module d'authentification
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash un mot de passe avec sel utilisant bcrypt

    Args:
        password: Le mot de passe à hasher

    Returns:
        bytes: Le mot de passe hashé
    """
    # Encode le mot de passe en bytes
    password_bytes = password.encode('utf-8')

    # Génère un sel et hash le mot de passe
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed


class Auth:
    """Classe Auth pour interagir avec la base de données d'authentification
    """

    def __init__(self):
        """Initialise une nouvelle instance Auth"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Enregistre un nouvel utilisateur dans la base de données

        Args:
            email: Email de l'utilisateur
            password: Mot de passe de l'utilisateur

        Returns:
            User: L'utilisateur créé

        Raises:
            ValueError: Si l'utilisateur existe déjà
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
