#!/usr/bin/env python3
"""
This module contains wait_n() coroutine to practice async operations
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This coroutine runs wait_random n times and returns a list 
        of delay times """

    tasks = [asyncio.create_task(wait_random(max_delay)) for nums in range(n)]

    results = await asyncio.gather(*tasks)

    return results
