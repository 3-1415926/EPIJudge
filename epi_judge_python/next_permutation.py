from typing import List

from test_framework import generic_test


def reverse_tail(perm: List[int], left: int):
    right = len(perm) - 1
    while left < right:
        perm[left], perm[right] = perm[right], perm[left]
        left += 1
        right -= 1

def next_permutation(perm: List[int]) -> List[int]:
    i = len(perm) - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1
    if i <= 0:
        return []
    j = i
    while j < len(perm) and perm[i - 1] < perm[j]:
        j += 1
    perm[i - 1], perm[j - 1] = perm[j - 1], perm[i - 1]
    reverse_tail(perm, i)
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
