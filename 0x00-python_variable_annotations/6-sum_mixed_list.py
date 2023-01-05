#!/usr/bin/env python3
"""Module contain sum_mixed function."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function takes mixed list and returns sum as floating num."""
    return float(sum(mxd_lst))
