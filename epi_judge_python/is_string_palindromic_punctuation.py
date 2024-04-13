import unicodedata
from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and unicodedata.category(s[l])[0] not in 'LN':
            l += 1
        while l < r and unicodedata.category(s[r])[0] not in 'LN':
            r -= 1
        if l < r and s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
