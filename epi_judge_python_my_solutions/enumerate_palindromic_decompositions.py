from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    def recursive_decompositions(start: int):
        if start >= len(text):
            results.append(cur_result.copy())
            return
        for i in range(start, len(text)):
            prefix = text[start:i + 1]
            if prefix == prefix[::-1]:
                cur_result.append(prefix)
                recursive_decompositions(i + 1)
                cur_result.pop()
    cur_result = []
    results = []
    recursive_decompositions(0)
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
