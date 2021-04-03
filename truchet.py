import numpy as np
from skimage.measure import block_reduce
from typing import List


def brightness_value(arr: np.ndarray):
    return arr.mean() / 255.


def optimal_point(brightness: float) -> float:
    if brightness < 0.25:
        return 0.
    elif brightness > 0.75:
        return 1.
    else:
        return 2. * brightness - 0.5


def color_of_tile(x: float, y: float, mid_point: float) -> int:
    is_in_area1: bool = y < (mid_point - 1) / mid_point * x + 1
    is_in_area2: bool = y < mid_point / (1 - mid_point) * (1 - x)
    if mid_point < 0.5:
        return 255 * (int(is_in_area1 or is_in_area2))
    else:
        return 255 * (int(is_in_area1 and is_in_area2))


def midpoint(t: float):
    return 0.25 + 0.5 * t


def truchet_tile(size: int, brightness: float, rotation: int = 0):
    ret = np.fromfunction(np.vectorize(lambda x, y: color_of_tile(x/size, y/size, midpoint(optimal_point(brightness)))),
                          (size, size))
    for _ in range(0, rotation):
        # Rotate matrix if other type is used
        ret = np.rot90(ret)
    return ret


def truchet_image(arr, size, pattern: List[List[int]]):
    brightness_arr = block_reduce(arr, (size, size), np.mean) / 255.
    new_mat = []
    n: int = len(pattern)
    m: int = len(pattern[0])
    for i, row in enumerate(brightness_arr):
        new_row = []
        for j, column in enumerate(row):
            new_row.append(truchet_tile(size, column, pattern[i % n][j % m]))
        new_mat.append(new_row)
    return np.block(new_mat)

