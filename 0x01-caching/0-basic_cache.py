#!/usr/bin/env python3
"""
caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    store and retrrive from dic
    """
    def put(self, key, item):
        """store
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve
        """
        return self.cache_data.get(key, None)
