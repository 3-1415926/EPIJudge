from test_framework import generic_test


def square_root(k: int) -> int:
    if k < 0: raise ValueError()
    bottom, top = 0, k
    while bottom < top:
        mid = (bottom + top + 1) // 2
        if mid * mid > k:
            top = mid - 1
        else:
            bottom = mid
    return bottom


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
