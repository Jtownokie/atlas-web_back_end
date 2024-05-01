#!/usr/bin/env python3
"""
This module contains wait_random() coroutine to practice async operations
"""

import asyncio
import random
import typing


async def wait_random(max_delay: int = 10) -> float:
    """ This coroutine waits for a random delay between 0 and max_delay """
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
