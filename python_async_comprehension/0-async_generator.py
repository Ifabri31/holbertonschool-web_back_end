#!/usr/bin/env python3
"""
Module Documented
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Documented
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
