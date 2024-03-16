#!/usr/bin/env python3
"""
This module defines a function sum_list that computes the sum of floats in a list.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of floats in a list.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of floats in the list.
    """
    return sum(input_list)

if __name__ == "__main__":
    sum_list = __import__('5-sum_list').sum_list

    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
