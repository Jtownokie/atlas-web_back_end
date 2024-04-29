#!/usr/bin/env python3
"""
This module contains the sum_list() function practicing type hints
"""

import typing
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ This function takes a list of floats and returns the sum of its values """
    return sum(input_list)
