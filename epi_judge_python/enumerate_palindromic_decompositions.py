from functools import cache
from typing import List

from test_framework import generic_test

def is_palindromic(text: str, left: int, right: int) -> bool:
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

@cache
def palindrome_decompositions(text: str, start: int = 0) -> List[List[str]]:
    if start >= len(text):
        return [[]]
    results = []
    for end in range(start, len(text)):
        if not is_palindromic(text, start, end):
            continue
        for remainder in palindrome_decompositions(text, end + 1):
            results.append([text[start:end + 1]] + remainder)
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
