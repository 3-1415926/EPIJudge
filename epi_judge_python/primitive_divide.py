from decimal import DivisionByZero
from test_framework import generic_test


def divide(x: int, y: int) -> int:
    if x < 0 or y < 0: raise ValueError('Non-negative only')
    if y == 0: raise DivisionByZero()
    quotient, mask = 0, 1
    while x >= y:
        y <<= 1
        mask <<= 1
    while mask > 0:
        if x >= y:
            quotient |= mask
            x -= y
        y >>= 1
        mask >>= 1
    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
