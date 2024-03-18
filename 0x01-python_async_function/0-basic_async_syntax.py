#!/usr/bin/env python3
"""
Async Coroutine Module
"""

import asyncio
import random
from typing import Optional

async def wait_random(max_delay: Optional[int] = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (inclusive). Defaults to 10.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main(max_delay: Optional[int] = 10) -> None:
    """
    Main function to test the wait_random coroutine.
    """
    print(await wait_random(max_delay))
    print(await wait_random(5))
    print(await wait_random(15))

if __name__ == "__main__":
    random.seed(1)  # Seed the random number generator for reproducibility
    asyncio.run(main())
