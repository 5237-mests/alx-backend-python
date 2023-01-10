#!/usr/bin/env python3
"""Module for task1
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asyncronous Generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
