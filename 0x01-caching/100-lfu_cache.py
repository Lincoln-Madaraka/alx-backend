#!/usr/bin/env python3
'''5. LFU Caching'''


BaseCaching = __import__('base_caching').BaseCaching


def find_lfu(cache):
    '''return the key that is least frequently used'''
    least_times = None
    least_used = None
    for key, t in cache.items():
        if least_times is None or t < least_times:
            least_times = t
            least_used = key
    return least_used


class LFUCache(BaseCaching):
    '''
    class LFUCache that inherits from BaseCaching and is a
    caching system which use least frequently used algorythim
    '''

    def __init__(self):
        '''initiate an instance'''
        super().__init__()
        self.lfu = dict()

    def put(self, key, item):
        '''Assigin the value of item to key using LFU Algorithm'''
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= self.MAX_ITEMS\
                and key not in self.cache_data:
            lfu = find_lfu(self.lfu)
            print('DISCARD: {}'.format(lfu))
            del self.cache_data[lfu]
            del self.lfu[lfu]
        if self.lfu.get(key):
            self.lfu[key] += 1
        else:
            self.lfu[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        '''Return the value in self.cache_data linked to key or None'''
        if self.cache_data.get(key):
            self.lfu[key] += 1
        return self.cache_data.get(key)
