from typing import List

from test_framework import generic_test


def find_first_missing_positive(A: List[int]) -> int:
    for i in range(len(A)):
        while 0 < A[i] <= len(A) and A[i] != A[A[i] - 1]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1         
    return len(A) + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('first_missing_positive_entry.py',
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
