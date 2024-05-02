#!/usr/bin/env python3
"""
This module contains async_generator() coroutine to practice async operations
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This coroutine loops 10 times async, waiting 1 second each time """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
