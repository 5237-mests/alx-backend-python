#!/usr/bin/env python3
"""Module for task1
"""
import random
import asyncio


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
