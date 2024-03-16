#!/usr/bin/env python3
"""
This module defines a function floor that returns the floor of a float.
"""

import math

def floor(n: float) -> int:
    """
    Return the floor of a float.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)

if __name__ == "__main__":
    floor = __import__('2-floor').floor

    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
