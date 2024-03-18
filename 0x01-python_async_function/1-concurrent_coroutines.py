#!/usr/bin/env python3
"""
Async Coroutine Module
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each call to wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
