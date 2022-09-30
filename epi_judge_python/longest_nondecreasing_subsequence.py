import bisect
from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    # [i] holds smallest ending element of subsequence of length (i + 1)
    min_last_of_len = []
    for a in A:
        i = bisect.bisect_right(min_last_of_len, a)
        if i >= len(min_last_of_len): min_last_of_len.append(a)
        else: min_last_of_len[i] = a
    return len(min_last_of_len)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
