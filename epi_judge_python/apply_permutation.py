from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        temp, j = A[i], perm[i]
        while j != i:
            A[j], temp = temp, A[j]
            perm[j], j = j, perm[j]
        A[j], perm[j] = temp, j


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
