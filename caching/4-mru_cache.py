#!/usr/bin/python3
"""
    MRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
        - put(): Setter Type Method
        - get(): Getter Type Method
    """

    RECENTKEY = None

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
            print(f"DISCARD: {MRUCache.RECENTKEY}")
            del self.cache_data[MRUCache.RECENTKEY]

        self.cache_data[key] = item
        MRUCache.RECENTKEY = key

    def get(self, key):
        """
            Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            MRUCache.RECENTKEY = key
            return self.cache_data[key]
