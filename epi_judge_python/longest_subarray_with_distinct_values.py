from collections import Counter
from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    num_duplicates = 0
    counter = Counter()
    best_start, best_end = start, end = 0, 0
    while True:
        if num_duplicates == 0 or start >= end:
            if best_end - best_start < end - start:
                best_start, best_end = start, end
            if end >= len(A):
                break
            counter[A[end]] += 1
            if counter[A[end]] == 2:
                num_duplicates += 1
            end += 1
        else:
            counter[A[start]] -= 1
            if counter[A[start]] == 1:
                num_duplicates -= 1
            start += 1            
    return best_end - best_start


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
