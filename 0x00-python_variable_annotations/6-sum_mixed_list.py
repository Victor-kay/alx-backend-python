#!/usr/bin/env python3
"""
This module defines a function sum_mixed_list that computes the sum of integers and floats in a mixed list.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of integers and floats in the list.
    """
    return sum(mxd_lst)

if __name__ == "__main__":
    sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
