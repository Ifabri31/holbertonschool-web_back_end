#!/usr/bin/env python3
"""
Module documented
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function documented
    """

    def multiply_by_multiplier(x: float) -> float:
        return x * multiplier

    return multiply_by_multiplier
