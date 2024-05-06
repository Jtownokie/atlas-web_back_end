#!/usr/bin/python3
"""
    FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ BasicCache defines:
        - put(): Setter Type Method
        - get(): Getter Type Method
    """

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
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            FirstInKey = list(self.cache_data.keys())[0]
            print(f"DISCARD: {FirstInKey}")
            del self.cache_data[FirstInKey]

    def get(self, key):
        """
            Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
