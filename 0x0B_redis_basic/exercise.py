#!/usr/bin/env python3
"""
Module pour la gestion du cache Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Décorateur qui compte le nombre d'appels à une méthode.

    Args:
        method: La méthode à décorer

    Returns:
        Callable: La méthode décorée avec compteur d'appels
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper qui incrémente le compteur avant d'appeler la méthode.
        """
        # Utilise le nom qualifié de la méthode comme clé
        key = method.__qualname__
        # Incrémente le compteur
        self._redis.incr(key)
        # Exécute la méthode originale
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Décorateur qui stocke l'historique des appels d'une méthode.

    Args:
        method: La méthode à décorer

    Returns:
        Callable: La méthode décorée avec historique des appels
    """
    @wraps(method)
    def wrapper(self, *args):
        """
        Wrapper qui stocke les entrées et sorties de la méthode.
        """
        # Clés pour stocker les entrées et sorties
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        
        # Stockage des arguments d'entrée
        self._redis.rpush(inputs_key, str(args))
        
        # Exécution de la méthode originale
        output = method(self, *args)
        
        # Stockage de la sortie
        self._redis.rpush(outputs_key, output)
        
        return output
    return wrapper


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

    @count_calls
    @call_history
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
        Récupère les données stockées dans Redis et
        les convertit si nécessaire.

        Args:
            key: La clé pour récupérer les données
            fn: Fonction optionnelle pour convertir les données

        Returns:
            Les données converties selon la fonction
            fournie ou les données brutes
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
