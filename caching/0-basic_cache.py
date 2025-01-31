#!/usr/bin/python3
""" 0-basic_cache """

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ Classe de cache de base qui hérite de BaseCaching """
    
    def put(self, key, item):
        """
        Assigne l'élément à la clé donnée dans le cache
        Args:
            key: la clé pour stocker l'élément
            item: l'élément à stocker
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Récupère l'élément associé à la clé donnée dans le cache
        Args:
            key: la clé de l'élément à récupérer
        Returns:
            L'élément associé à la clé, ou None si la clé n'existe pas
        """
        return self.cache_data.get(key, None)
