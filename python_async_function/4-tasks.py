#!/usr/bin/env python3
"""
This module contains task_wait_n() coroutine to practice async operations
"""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This coroutine runs wait_random n times and returns a list
        of delay times """

    tasks = [task_wait_random(max_delay) for nums in range(n)]

    results = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
