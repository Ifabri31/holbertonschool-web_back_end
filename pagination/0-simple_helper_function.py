#!/usr/bin/env python3
"""
Module documented
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function documented
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
