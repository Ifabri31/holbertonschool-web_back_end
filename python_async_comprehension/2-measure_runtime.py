#!/usr/bin/env python3
"""
Module documented
"""
import asyncio
import time
async_comprehsion = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Documented
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehsion() for i in range(4)))
    end_time = time.time()
    return end_time - start_time
