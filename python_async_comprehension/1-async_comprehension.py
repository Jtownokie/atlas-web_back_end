#!/usr/bin/env python3
"""
This module contains async_comprehension() coroutine to practice async
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This coroutine uses async comprehension to collect 10 random nums """
    result = []

    async for i in async_generator():
        result.append(i)

    return result
