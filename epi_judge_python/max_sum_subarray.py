from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    max_overall = 0
    max_trailing = 0
    for a in A:
        max_trailing = max(max_trailing + a, 0)
        max_overall = max(max_overall, max_trailing)
    return max_overall


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
