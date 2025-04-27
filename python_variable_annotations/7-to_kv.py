#!/usr/bin/env python3
"""
Module documented
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v*v))
