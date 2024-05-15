from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    ai, bi = 0, 0
    result = []
    while ai < len(A) and bi < len(B):
        if A[ai] < B[bi]:
            ai += 1
        elif A[ai] > B[bi]:
            bi += 1
        else:
            if not result or result[-1] != A[ai]:
                result.append(A[ai])
            ai += 1
            bi += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
