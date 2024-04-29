#!/usr/bin/env python3
"""
This module contains the make_multiplier() function practicing type hints
"""

import typing
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function takes a float and returns a function """
    def func(num: float) -> float:
        return num * multiplier

    return func

