#!/usr/bin/env python3
'''2. LIFO Caching'''


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    class LIFOCache that inherits from BaseCaching and is a
    caching system which implement last in first out algorithm
    '''
    def __init__(self):
        '''initiate an instance'''
        super().__init__()
        self.stack = list()

    def put(self, key, item):
        '''Assigin the value of item to key using LIFO Algorithm'''
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= self.MAX_ITEMS\
                and key not in self.cache_data:
            old_key = self.stack.pop()
            print('DISCARD: {}'.format(old_key))
            del self.cache_data[old_key]
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Return the value in self.cache_data linked to key or None'''
        return self.cache_data.get(key)
