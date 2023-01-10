#!/usr/bin/env python3
"""Module for task1
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Function for async comrehension"""
    mylist = [el async for el in async_generator()]
    return mylist
