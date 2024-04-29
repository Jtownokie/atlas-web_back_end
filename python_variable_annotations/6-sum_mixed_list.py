#!/usr/bin/env python3
"""
This module contains the sum_mixed_list() function practicing type hints
"""

import typing
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ This function takes a list of ints and floats and returns its sum """
    return sum(mxd_list)
