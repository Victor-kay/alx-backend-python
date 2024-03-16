#!/usr/bin/env python3
"""
This module defines a function add that takes two floats and returns their sum.
"""

def add(a: float, b: float) -> float:
    """
    Return the sum of two floats.

    Args:
        a (float): The first float.
        b (float): The second float.

    Returns:
        float: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    add = __import__('0-add').add

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
