#!/usr/bin/env python3
"""This module contains the implementation of
one of the caching policy, LFU - Least Frequently
Used"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class oimplementation of LRU cache policy"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add new item to cache dict"""
        if key is None or item is None:
            return
        # If new item is being added to the cache
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_item = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded_item[0]))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Access cache staorage and move recently accessed data
        to the end"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
