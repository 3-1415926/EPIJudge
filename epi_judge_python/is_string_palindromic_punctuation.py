import string
from test_framework import generic_test


ALPHANUMERIC = set(string.ascii_letters) | set(string.digits)


def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while True:
        while i < j and s[i] not in ALPHANUMERIC: i += 1
        while i < j and s[j] not in ALPHANUMERIC: j -= 1
        if i >= j: break
        if s[i].lower() != s[j].lower(): return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
