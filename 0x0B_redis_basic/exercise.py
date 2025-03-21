#!/usr/bin/env python3
"""
Module pour la gestion du cache Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, 
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Récupère les données stockées dans Redis et les convertit si nécessaire.

        Args:
            key: La clé pour récupérer les données
            fn: Fonction optionnelle pour convertir les données

        Returns:
            Les données converties selon la fonction fournie ou les données brutes
        """
        # Récupération des données de Redis
        data = self._redis.get(key)
        
        # Si aucune donnée n'est trouvée, retourne None
        if data is None:
            return None
        
        # Si une fonction de conversion est fournie, l'applique
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Récupère une chaîne de caractères stockée dans Redis.

        Args:
            key: La clé pour récupérer les données

        Returns:
            str: La chaîne de caractères décodée
        """
        # Utilise get avec une fonction lambda pour décoder en UTF-8
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Récupère un entier stocké dans Redis.

        Args:
            key: La clé pour récupérer les données

        Returns:
            int: La valeur convertie en entier
        """
        # Utilise get avec une fonction lambda pour convertir en int
        return self.get(key, fn=int)
