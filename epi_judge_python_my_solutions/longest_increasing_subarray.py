import collections
from typing import List

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A: List[int]) -> Subarray:
    if len(A) == 0: return Subarray(0, -1)
    max_start, max_len = 0, 1
    cur_start = 0
    while cur_start + max_len < len(A):
        for i in range(cur_start + max_len, cur_start, -1):
            if A[i - 1] >= A[i]:
                cur_start = i
                break
        else:
            i = cur_start + max_len + 1
            while i < len(A) and A[i - 1] < A[i]:
                i += 1
            max_start, max_len, cur_start = cur_start, i - cur_start, i
    return Subarray(max_start, max_start + max_len - 1)


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_increasing_subarray.py',
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
