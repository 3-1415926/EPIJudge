from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    result = perm.copy()
    i = len(result) - 2
    while i >= 0 and result[i] >= result[i + 1]: i -= 1
    if i < 0: return []
    j = i
    while j < len(result) - 1 and result[i] < result[j + 1]: j += 1
    result[i], result[j] = result[j], result[i]
    i, j = i + 1, len(result) - 1
    while i < j:
        result[i], result[j] = result[j], result[i]
        i, j = i + 1, j - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
