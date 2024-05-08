#!/usr/bin/python3
"""
    LRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
        - put(): Setter Type Method
        - get(): Getter Type Method
    """

    def __init__(self):
        """
            Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """
            Add an item in the cache
        """
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = value

    def get(self, key):
        """
            Get an item by key
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value

        return None
