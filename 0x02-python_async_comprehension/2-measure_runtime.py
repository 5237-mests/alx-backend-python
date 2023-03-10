#!/usr/bin/env python3
"""Module for task2
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function measuring time of comprehensed function"""
    t1 = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    t2 = time()
    return t2 - t1
