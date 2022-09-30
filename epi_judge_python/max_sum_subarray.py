from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    max_sum = 0
    max_sum_up_to = 0
    for i in range(len(A)):
        max_sum_up_to = max(max_sum_up_to, 0) + A[i]
        max_sum = max(max_sum, max_sum_up_to)
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
