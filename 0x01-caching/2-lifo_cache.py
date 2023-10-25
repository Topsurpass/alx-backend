#!/usr/bin/env python3
"""This module contains the implementation of the LIFO -
Last In First Out caching policy"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """clas that implementd LIFO cache policy"""

    def __init__(self):
        """Initialize object instances at creation"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add new item to the cache storage"""
        if key is None or item is None:
            return
        # If new key is being added
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_item = self.cache_data.popitem(last=True)
                print('DISCARD: {}'.format(discarded_item[0]))

        # If a key's value is being updated, update and move it to the last
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Get data from cache storage"""
        return self.cache_data.get(key, None)
