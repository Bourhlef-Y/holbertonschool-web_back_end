#!/usr/bin/env python3
"""
Module pour la gestion du cache Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Classe Cache qui gère une instance Redis pour le stockage de données.
    Cette classe permet de stocker des données de différents types dans Redis
    et génère des clés uniques pour chaque entrée.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance Cache.
        Crée une connexion Redis et nettoie la base de données.
        """
        # Création d'une instance Redis privée
        self._redis = redis.Redis()
        # Nettoyage de la base de données Redis au démarrage
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stocke les données dans Redis avec une clé générée aléatoirement.

        Args:
            data: Les données à stocker (peut être str, bytes, int ou float)

        Returns:
            str: La clé générée sous laquelle les données sont stockées

        Example:
            >>> cache = Cache()
            >>> key = cache.store("hello")
            >>> print(cache._redis.get(key))
            b'hello'
        """
        # Génération d'une clé unique avec uuid4
        key = str(uuid.uuid4())

        # Stockage des données dans Redis avec la clé générée
        self._redis.set(key, data)

        # Retour de la clé pour référence future
        return key
