#!/usr/bin/env python3
'''3. LRU Caching'''
import time


BaseCaching = __import__('base_caching').BaseCaching


def find_lru(cache):
    '''return the key that is least recently used'''
    least_time = time.time()
    least_used = None
    for key, t in cache.items():
        if t < least_time:
            least_time = t
            least_used = key
    return least_used


class LRUCache(BaseCaching):
    '''
    class LRUCache that inherits from BaseCaching and is a
    caching system which use least recently used algorythim
    '''

    def __init__(self):
        '''initiate an instance'''
        super().__init__()
        self.lru = dict()

    def put(self, key, item):
        '''Assigin the value of item to key using LRU Algorithm'''
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= self.MAX_ITEMS\
                and key not in self.cache_data:
            lru = find_lru(self.lru)
            print('DISCARD: {}'.format(lru))
            del self.cache_data[lru]
            del self.lru[lru]
        self.lru[key] = time.time()
        self.cache_data[key] = item

    def get(self, key):
        '''Return the value in self.cache_data linked to key or None'''
        if self.cache_data.get(key):
            self.lru[key] = time.time()
        return self.cache_data.get(key)
