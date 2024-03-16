#!/usr/bin/env python3
"""
This module defines a function element_length that takes a list and returns
a list of tuples containing each element of the input list and its length.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element of the input list and its length.

    Args:
        lst (Iterable[Sequence]): The input list.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each element of
        the input list and its length.
    """
    return [(i, len(i)) for i in lst]

if __name__ == "__main__":
    element_length =  __import__('9-element_length').element_length

    print(element_length.__annotations__)
