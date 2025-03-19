import asyncio

import time


def heavy_computation_work() -> int:
    n = 0
    for i in range(60):
        n += i
        time.sleep(1)
    return n


async def heavy_computation_work_async() -> int:
    n = 0
    for i in range(60):
        n += i
        await asyncio.sleep(1)
    return n
