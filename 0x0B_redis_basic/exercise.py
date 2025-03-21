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
        key = method.__qualname__
        self._redis.incr(key)
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


def replay(method: Callable) -> None:
    """
    Affiche l'historique des appels d'une méthode.

    Args:
        method: La méthode dont l'historique doit être affiché
    """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    # Récupération des entrées et sorties
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    # Affichage du nombre d'appels
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    # Affichage des entrées et sorties
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> "
              f"{output_data.decode('utf-8')}")


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
        self._redis = redis.Redis()
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
        key = str(uuid.uuid4())
        self._redis.set(key, data)
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
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Récupère une chaîne de caractères stockée dans Redis.

        Args:
            key: La clé pour récupérer les données

        Returns:
            str: La chaîne de caractères décodée
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Récupère un entier stocké dans Redis.

        Args:
            key: La clé pour récupérer les données

        Returns:
            int: La valeur convertie en entier
        """
        return self.get(key, fn=int)
