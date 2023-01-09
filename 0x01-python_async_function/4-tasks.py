#!/usr/bin/env python3
"""Module for task4
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes concurrent async await"""
    task_wait_random(max_delay)

    wait_times = await asyncio.gather(
        *list(map(lambda k: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
