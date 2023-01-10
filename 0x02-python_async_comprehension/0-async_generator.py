#!/usr/bin/env python3
"""Module for task1
"""
from random import uniform
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asyncronous Generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
