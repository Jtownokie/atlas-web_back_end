#!/usr/bin/env python3
"""
This module contains the to_kv() function practicing type hints
"""

import typing
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """ This function takes a str and int OR float and returns tuple """
    return (k, v * v)
