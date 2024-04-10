from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    max_digit_weight = 1
    while x >= max_digit_weight * 10:
        max_digit_weight *= 10
    while x:
        if x // max_digit_weight != x % 10:
            return False
        x %= max_digit_weight
        x //= 10
        max_digit_weight //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
