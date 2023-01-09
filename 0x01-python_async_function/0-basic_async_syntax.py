#!/usr/bin/env python3
"""Module
"""

import asyncio


import random


async def wait_random(max_delay: int = 10) -> float:
    """Function awaits for a given random time and return it."""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
