#!/usr/bin/env python3
"""
This module defines a function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the given multiplier.
    """

    def multiplier_func(x: float) -> float:
        """
        Multiply a float by the given multiplier.

        Args:
            x (float): The float to be multiplied.

        Returns:
            float: The result of multiplying the input float by the multiplier.
        """
        return x * multiplier

    return multiplier_func


if __name__ == "__main__":
    make_multiplier = __import__('8-make_multiplier').make_multiplier

    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
