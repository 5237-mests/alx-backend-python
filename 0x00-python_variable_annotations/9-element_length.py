#!/usr/bin/env python3
"""Module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """el length"""
    return [(i, len(i)) for i in lst]