#!/usr/bin/env python3
""" This module contains the Cache class for Redis access """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Counts number of calls of method """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Keeps Call History of wrapped method """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


class Cache():
    """ This Class defines a Redis cache """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores a string in Redis Cache """
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Callable = None):
        """ Retrieves byte string from Database """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, data: bytes) -> str:
        """ Decodes byte string data to str """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """ Decodes byte string data to int """
        return int.from_bytes(data, "big")


def replay(method: Callable):
    """ This method provides information on call count and call history """
    self = method.__self__
    qualname = method.__qualname__

    input_key = qualname + ":inputs"
    output_key = qualname + ":outputs"

    inputs = self._redis.lrange(input_key, 0, -1)
    outputs = self._redis.lrange(output_key, 0, -1)

    print(f"{qualname} was called {len(inputs)} times:")
    for i, (input_, output) in enumerate(zip(inputs, outputs)):
        print(f"{qualname}(*{input_.decode('utf-8')})"
              f" -> {output.decode('utf-8')}")
