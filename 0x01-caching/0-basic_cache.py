#!/usr/bin/python3
"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """the class for baseCaching"""

    def put(self, key, item):
        """putting to a cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get a value from the cache"""
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
