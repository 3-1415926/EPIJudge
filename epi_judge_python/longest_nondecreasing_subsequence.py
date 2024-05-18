import bisect
from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    min_end_for_len = [float('inf')] * len(A)
    for a in A:
        min_end_for_len[bisect.bisect(min_end_for_len, a)] = a
    return bisect.bisect_left(min_end_for_len, float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
