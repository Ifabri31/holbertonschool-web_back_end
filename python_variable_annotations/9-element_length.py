#!/usr/bin/env python3
"""
Module documented
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function documented
    """
    return [(i, len(i)) for i in lst]
