#!/usr/bin/env python3
"""Module contain to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function retrurn mixed tuple"""
    return tuple((k, float(v**2)))
