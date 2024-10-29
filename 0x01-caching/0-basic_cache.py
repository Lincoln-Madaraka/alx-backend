#!/usr/bin/env python3
'''0. Basic dictionary'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    BasicCache inherits from BaseCaching and extend it
    '''
    def __init__(self):
        '''Initiate an instant'''
        super().__init__()

    def put(self, key, item):
        '''assign item to key in cache_data'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Return the value in self.cache_data linked to key or None'''
        return self.cache_data.get(key)
