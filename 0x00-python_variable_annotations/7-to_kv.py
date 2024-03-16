#!/usr/bin/env python3
"""
This module defines a function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple. The first element of the tuple is the string k.
The second element is the square of the int/float v and is annotated as a float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Construct a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v as a float.
    """
    return k, float(v) ** 2

if __name__ == "__main__":
    to_kv = __import__('7-to_kv').to_kv

    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
