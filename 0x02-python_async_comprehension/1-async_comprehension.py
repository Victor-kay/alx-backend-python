#!/usr/bin/env python3
"""
Async Comprehension
"""

import random
from typing import List

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: List of 10 random numbers.
    """
    async def async_generator():
        """
        Generates random numbers asynchronously.
        """
        for _ in range(10):
            await yield_(random.uniform(0, 10))

    async_result = [number async for number in async_generator()]
    return async_result
