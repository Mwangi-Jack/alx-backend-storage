#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

"""Test 1"""
# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))



"""test 2"""
# cache = Cache()

# TEST_CASES = {
# 	b"foo": None,
# 	123: int,
# 	"bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
# 	key = cache.store(value)
# 	assert cache.get(key, fn=fn) == value

# print("All test cases passed.")

"""test 3"""

# cache.store(b"first")
# print(cache.get(cache.store.__qualname__))

# cache.store(b"second")
# cache.store(b"third")
# print(cache.get(cache.store.__qualname__))


"""test 4"""

# s1 = cache.store("first")
# print(s1)
# s2 = cache.store("secont")
# print(s2)
# s3 = cache.store("third")
# print(s3)

# inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
# outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

# print("inputs: {}".format(inputs))
# print("outputs: {}".format(outputs))

"""test 5"""
cache.store("foo")
cache.store("bar")
cache.store(42)

cache.replay(cache.store)
