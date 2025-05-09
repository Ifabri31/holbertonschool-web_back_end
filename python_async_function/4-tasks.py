#!/usr/bin/env python3
"""
4-tasks.py
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function documented
    """
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    list = await asyncio.gather(*tasks)
    return sorted(list)
