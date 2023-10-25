#!/usr/bin/env python3
"""This module contains the implementation of the FIFO -
First In First Out caching policy"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Class definition of the FIFO caching policy"""

    def __init__(self):
        """Initialize the objects"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """new data to the catch dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        """if cache storage is full"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_item = self.cache_data.popitem(last=False)
            print('DISCARD: {}'.format(discarded_item[0]))

    def get(self, key):
        """Access data from the cache system"""
        return self.cache_data.get(key, None)
