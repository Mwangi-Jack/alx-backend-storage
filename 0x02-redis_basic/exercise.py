#!/usr/bin/env python3
"""file: exercise.py -> defines the Cache class """

import uuid
from typing import Union
import redis


class Cache:
    """
    Cache class defines two methods the initializaiton method
    and the store method
    """

    def __init__(self):
        """
        this method initializes the class with a private
        variable '_redis' which holds the redis instance
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method takes in a 'data' argument generates a random key
        ,stores the input data in Redis using the random keyand returns
        the key in a string format
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
