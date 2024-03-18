#!/usr/bin/env python3
"""
Tasks Module
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds for each call to task_wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    import asyncio

    async def test(n: int, max_delay: int) -> None:
        print(await task_wait_n(n, max_delay))

    asyncio.run(test(5, 6))
