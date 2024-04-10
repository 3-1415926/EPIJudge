import math
from test_framework import generic_test

def square_root(x: float) -> float:
    if x < 0: raise ValueError()
    bottom, top = (0, 1) if x < 1 else (1, x)
    while not math.isclose(bottom, top):
        mid = (bottom + top) / 2
        if mid * mid > x:
            top = mid
        else:
            bottom = mid
    return bottom


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
