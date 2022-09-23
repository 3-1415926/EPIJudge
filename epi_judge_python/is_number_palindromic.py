from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x < 0: return False
    if x > 0 and x % 10 == 0: return False
    y = 0
    while x > y:
        y = y * 10 + x % 10
        if x == y: break
        x //= 10
    return x == y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
