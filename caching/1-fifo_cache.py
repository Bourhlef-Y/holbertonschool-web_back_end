#!/usr/bin/python3
""" 1-fifo_cache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
