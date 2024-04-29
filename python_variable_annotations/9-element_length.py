#!/usr/bin/env python3
"""
This module contains the element_length() function practicing type hints
"""

import typing
from typing import List, Union, Tuple, Callable, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function takes any Sequence and returns a list of tuples """
    return [(i, len(i)) for i in lst]
