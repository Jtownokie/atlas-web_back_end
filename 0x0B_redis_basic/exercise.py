#!/usr/bin/env python3
""" This module contains the Cache class for Redis access """
import redis
from uuid import uuid4
from typing import Union


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
