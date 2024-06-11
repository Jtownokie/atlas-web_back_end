#!/usr/bin/env python3
""" This module contains the Cache class for Redis access """
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache():
    """ This Class defines a Redis cache """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
