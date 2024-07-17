#!/usr/bin/env python3
"""file: exercise.py -> defines the Cache class """

import uuid
from functools import wraps
from typing import Any, Callable, Optional, Union
import redis


def count_calls(method: Callable) -> Callable:
    """
    This function is a decorator that takes in  a single callable
    'method' and returns  a callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__

        self._redis.incr(key)

        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    This function is a decorator function that takes in a single
    'callable' function and returns a callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key_input: str = f'{method.__qualname__}:inputs'
        key_output: str = f'{method.__qualname__}:outputs'

        self._redis.rpush(key_input, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(key_output, output)

        return output

    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method takes in a 'data' argument generates a random key
        ,stores the input data in Redis using the random keyand returns
        the key in a string format
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        This function takes in a  string 'key' and an optional callable 'fn
        """

        data = self._redis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieves the data and decode it as UTF-8 string"""
        return self.get(key, fn=lambda d: d.decode("uft-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieves the data and convert it to integer"""
        return self.get(key, fn=int)

def replay(self, method: Callable) -> None:
    """this function retrieves the history"""
    key_inputs = f"{method.__qualname__}:inputs"
    key_outputs = f"{method.__qualname__}:outputs"

    inputs = self._redis.lrange(key_inputs, 0, -1)
    outputs = self._redis.lrange(key_outputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        input_str = inp.decode()
        output_str = out.decode()
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")
