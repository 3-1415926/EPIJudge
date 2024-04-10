from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    if len(perm) != len(A): raise ValueError()
    for i in range(len(A)):
        carry = A[i]
        j = perm[i]
        while j != i:
            A[j], carry = carry, A[j]
            perm[j], j = j, perm[j]
        A[j] = carry
        perm[j] = j


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
