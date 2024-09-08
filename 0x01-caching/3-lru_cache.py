#!/usr/bin/python3

"""
2. LRU caching
"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class LRUCache(BaseCaching):
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
            # print(the_list)
            if len(the_list) > self.MAX_ITEMS:
                disc = the_list.pop(0)
                del self.cache_data[disc]
                print(f"DISCARD: {disc}")

    def get(self, key):
        """getting from cache"""
        the_list = self.list
        if key and key in self.cache_data.keys():
            the_list.remove(key)
            the_list.append(key)
            return self.cache_data.get(key)
        return None
