#!usr/bin/env python3
"""This module contains one of the common caching policy
LFU - Least Frequently Used"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class implementation of LFU cache policy"""
    def __init__(self) -> None:
        """Initialize of class instance on creation """
        super().__init__()
        self.track_dict = {}

    def put(self, key, item):
        """Add new item in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                pop_item = min(self.track_dict, key=self.track_dict.get)
                self.track_dict.pop(pop_item)
                self.cache_data.pop(pop_item)
                print("DISCARD: {}".format(pop_item))

            if key not in self.track_dict:
                self.track_dict[key] = 0
            else:
                self.track_dict[key] += 1

    def get(self, key):
        """Acces the cache storage for item"""
        if key is None or key not in self.cache_data:
            return None
        self.track_dict[key] += 1
        return self.cache_data.get(key)
