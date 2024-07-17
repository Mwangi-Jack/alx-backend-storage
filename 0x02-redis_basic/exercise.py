#!/usr/bin/env python3
"""Cache class"""

import uuid
import redis


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """
        This method takes in a 'data' argument generates a random key
        ,stores the input data in Redis using the random keyand returns
        the key in a string format
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
