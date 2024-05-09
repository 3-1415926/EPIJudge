from test_framework import generic_test


def square_root(k: int) -> int:
    assert k >= 0
    left, right = 0, k
    while left < right:
        mid = left + (right - left + 1) // 2
        if mid * mid > k:
            right = mid - 1
        else:
            left = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
