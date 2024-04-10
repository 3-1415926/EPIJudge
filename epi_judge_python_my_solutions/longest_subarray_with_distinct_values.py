from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    max_distinct = 0
    cur_distinct = set()
    i = 0
    for j in range(len(A)):
        while A[j] in cur_distinct:
            cur_distinct.discard(A[i])
            i += 1
        assert i <= j
        cur_distinct.add(A[j])
        max_distinct = max(max_distinct, len(cur_distinct))
    return max_distinct


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
