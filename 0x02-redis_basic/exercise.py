#!/usr/bin/env python3
"""Cache class"""

import uuid
import redis


class Cache:
    """
    Cache class defines two methods the initializaiton method
    and the store method
    """

    def __init__(self: "Cache") -> None:
        """
        this method initializes the class with a private
        variable '_redis' which holds the redis instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | float | int) -> str:
        """
        This method takes in a 'data' argument generates a random key
        ,stores the input data in Redis using the random keyand returns
        the key in a string format
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
