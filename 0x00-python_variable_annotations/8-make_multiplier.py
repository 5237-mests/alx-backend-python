#!/usr/bin/env python3
"""Module contain function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return multiplier function"""
    def retuerned_function(returned_function_argument):
        return returned_function_argument * multiplier
    return (retuerned_function)
