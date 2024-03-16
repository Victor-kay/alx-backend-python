#!/usr/bin/env python3
"""
This module defines a function safe_first_element that returns the first element of a sequence safely.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Return the first element of a sequence safely.

    Args:
        lst (Sequence): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

if __name__ == "__main__":
    safe_first_element =  __import__('100-safe_first_element').safe_first_element

    print(safe_first_element.__annotations__)
