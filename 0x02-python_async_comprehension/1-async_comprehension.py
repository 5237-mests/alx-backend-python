#!/usr/bin/env python3
"""Module for task1
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function for async comrehension"""
    return [el async for el in async_generator()]
