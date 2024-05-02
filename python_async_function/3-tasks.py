#!/usr/bin/env python3
"""
This module contains task_wait_random() function to practice async operations
"""

import asyncio
import time
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ This function returns a Task object """
    new_task = asyncio.create_task(wait_random(max_delay))

    return new_task
