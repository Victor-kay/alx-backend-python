#!/usr/bin/env python3
"""
Async Comprehension Module
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator coroutine.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [random_num async for random_num in async_generator()]
