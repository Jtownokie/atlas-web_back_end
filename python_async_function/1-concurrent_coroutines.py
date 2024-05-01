#!/usr/bin/env python3
"""
This module contains wait_n() coroutine to practice async operations
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delay_list = []

    for i in range(0, n):
        delay_time = await wait_random(max_delay)
        delay_list.append(delay_time)

    return delay_list
