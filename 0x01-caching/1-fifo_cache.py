#!/usr/bin/python3

"""
1. FIFO caching
"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """
    Fifo caching
    """

    def __init__(self):
        super().__init__()
        self.list = []

    def put(self, key, item):
        """put into cache"""
        the_list = self.list
        if key and item:
            if key in self.cache_data.keys():
                the_list.remove(key)
            self.cache_data[key] = item
            the_list.append(key)
            if len(the_list) > self.MAX_ITEMS:
                disc = the_list.pop(0)
                del self.cache_data[disc]
                print(f"DISCARD: {disc}")

    def get(self, key):
        """getting from cache"""
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
