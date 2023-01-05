#!/usr/bin/env python3
"""Module contain sum_mixed function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
