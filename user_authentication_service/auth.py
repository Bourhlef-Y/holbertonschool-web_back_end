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
