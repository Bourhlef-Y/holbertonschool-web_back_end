#!/usr/bin/env python3
"""Module d'authentification
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


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


def _generate_uuid() -> str:
    """Génère un UUID unique

    Returns:
        str: La représentation string de l'UUID
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Vérifie si les identifiants de connexion sont valides

        Args:
            email: Email de l'utilisateur
            password: Mot de passe à vérifier

        Returns:
            bool: True si les identifiants sont valides, False sinon
        """
        try:
            user = self._db.find_user_by(email=email)
            password_bytes = password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Crée une session pour l'utilisateur

        Args:
            email: Email de l'utilisateur

        Returns:
            str: ID de session si l'utilisateur existe, None sinon
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Récupère un utilisateur à partir de son ID de session

        Args:
            session_id: ID de session à rechercher

        Returns:
            User: L'utilisateur correspondant à l'ID de session
            None: Si l'ID de session est None ou si aucun utilisateur
            n'est trouvé
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Détruit la session d'un utilisateur

        Args:
            user_id: ID de l'utilisateur dont la session doit être détruite
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Génère un token de réinitialisation de mot de passe

        Args:
            email: Email de l'utilisateur

        Returns:
            str: Token de réinitialisation

        Raises:
            ValueError: Si l'utilisateur n'existe pas
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError
