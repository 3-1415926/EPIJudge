from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    assert len(A) >= m + n
    while m > 0 or n > 0:
        if m > 0 and (n <= 0 or A[m - 1] >= B[n - 1]):
            m -= 1
            A[m + n] = A[m]
        else:
            n -= 1
            A[m + n] = B[n]


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
