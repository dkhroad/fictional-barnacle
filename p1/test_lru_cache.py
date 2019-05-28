from lru_cache import *
import unittest

class TestLRU_Cache(unittest.TestCase):

    def test_LRU_Cache(self):
        cache = LRU_Cache(5)

        cache.set(1,1)
        cache.set(2,2)
        self.assertEqual( cache.get(1) , 1)
        self.assertEqual( cache.get(2) , 2)
        self.assertEqual( cache.get(3) , -1)
        cache.set(3,3)
        cache.set(4,4)
        cache.set(5,5)
        self.assertEqual( cache.get(1) , 1)
        print(cache.cache)
        cache.set(6,6)
        print(cache.cache)
        self.assertEqual( cache.get(3) , -1)
        self.assertEqual( cache.get(6) , 6)

