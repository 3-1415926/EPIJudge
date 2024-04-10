from test_framework import generic_test


def reverse(x: int) -> int:
    is_negative = x < 0
    x = abs(x)
    y = 0
    while x > 0:
        y = y * 10 + x % 10
        x //= 10
    return -y if is_negative else y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
