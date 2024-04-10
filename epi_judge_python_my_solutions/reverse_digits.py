from test_framework import generic_test


def reverse(x: int) -> int:
    result = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)
    while x > 0:
        result = result * 10 + x % 10
        x //= 10
    return result * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
