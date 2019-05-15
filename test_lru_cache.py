from lru_cache import *

def test_LRU_Cache():
    cache = LRU_Cache(5)

    cache.set(1,1)
    cache.set(2,2)
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(3) == -1
    cache.set(3,3)
    cache.set(4,4)
    cache.set(5,5)
    assert cache.get(1) == 1
    print(cache.cache)
    cache.set(6,6)
    print(cache.cache)
    assert cache.get(3) == -1
    assert cache.get(6) == 6

