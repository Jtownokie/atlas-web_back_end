#!/usr/bin/env python3
"""
This module contains measure_time() coroutine to practice async operations
"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ This function measures how long it takes to run wait_n """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start

    return elapsed / n
