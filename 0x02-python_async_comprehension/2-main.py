#!/usr/bin/env python3

import asyncio
from typing import Union

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main() -> Union[int, float]:
    """
    Runs measure_runtime coroutine and prints the result.
    """
    return await measure_runtime()

print(
    asyncio.run(main())
)
