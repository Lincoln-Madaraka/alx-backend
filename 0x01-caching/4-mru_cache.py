#!/usr/bin/env python3
'''4. MRU Caching'''
import time


BaseCaching = __import__('base_caching').BaseCaching


def find_mru(cache):
    '''return the key that is most recently used'''
    most_time = 0
    most_used = None
    for key, t in cache.items():
        if t > most_time:
            most_time = t
            most_used = key
    return most_used


class MRUCache(BaseCaching):
    '''
    class MRUCache that inherits from BaseCaching and is a
    caching system which use most recently used algorythim
    '''

    def __init__(self):
        '''initiate an instance'''
        super().__init__()
        self.mru = dict()

    def put(self, key, item):
        '''Assigin the value of item to key using MRU Algorithm'''
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= self.MAX_ITEMS\
                and key not in self.cache_data:
            mru = find_mru(self.mru)
            print('DISCARD: {}'.format(mru))
            del self.cache_data[mru]
            del self.mru[mru]
        self.mru[key] = time.time()
        self.cache_data[key] = item

    def get(self, key):
        '''Return the value in self.cache_data linked to key or None'''
        if self.cache_data.get(key):
            self.mru[key] = time.time()
        return self.cache_data.get(key)
