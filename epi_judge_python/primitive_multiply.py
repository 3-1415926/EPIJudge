from test_framework import generic_test


def add(x: int, y: int) -> int:
    assert x >= 0 and y >= 0
    while y:
        x, y = x ^ y, (x & y) << 1
    return x


def multiply(x: int, y: int) -> int:
    result = 0
    while x:
        if x & 1 != 0:
            result = add(result, y)
        x, y = x >> 1, y << 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
