import collections
from typing import List

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A: List[int]) -> Subarray:
    best_start, best_end = 0, 0
    start = 0
    for end in range(1, len(A) + 1):
        if end >= len(A) or A[end] <= A[end - 1]:
            if best_end - best_start < end - start:
                best_start, best_end = start, end
            start = end    
    return Subarray(best_start, best_end - 1)


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_increasing_subarray.py',
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
