#!/usr/bin/env python3
"""
This module defines a function safely_get_value that safely retrieves a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value for.
        default (Union[T, None], optional): The default value to return if the key is not present.
            Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key in the dictionary if it exists,
            otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

if __name__ == "__main__":
    safely_get_value = __import__('101-safely_get_value').safely_get_value
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
