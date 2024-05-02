#!/usr/bin/env python3
"""
This module contains measure_runtime() coroutine to practice async
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ This coroutine measures runtime on async comprehension """
    start = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    elapsed = time.perf_counter() - start

    return elapsed
