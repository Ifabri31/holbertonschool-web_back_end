#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function documented
    """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    list = await asyncio.gather(*tasks)
    return sorted(list)
