from test_framework import generic_test


def divide(x: int, y: int) -> int:
    assert x >= 0 and y > 0
    result = 0
    bit = 1
    while x >= y << 1:
        y <<= 1
        bit <<= 1
    while bit > 0:
        if x >= y:
            x -= y
            result |= bit
        y >>= 1
        bit >>= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
