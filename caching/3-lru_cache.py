#!/usr/bin/python3
"""
    LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
        - put(): Setter Type Method
        - get(): Getter Type Method
    """

    LASTINKEY = None

    def __init__(self):
        """
            Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
            Add an item in the cache
        """
        if key is None or item is None:
            return
        elif (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
              key not in self.cache_data.keys()):
            print(f"DISCARD: {LRUCache.LASTINKEY}")
            del self.cache_data[LRUCache.LASTINKEY]

        self.cache_data[key] = item
        LRUCache.LASTINKEY = key

    def get(self, key):
        """
            Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
