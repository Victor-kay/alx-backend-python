from typing import Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


if __name__ == "__main__":
    zoom_array =  __import__('102-type_checking').zoom_array

    print(zoom_array.__annotations__)
