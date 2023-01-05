#!/usr/bin/env python3
"""Module 10's tsk"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function return first element of sequence if available"""
    if lst:
        return lst[0]
    else:
        return None
