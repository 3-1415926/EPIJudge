from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    longest_range = 0
    entries = set(A)
    for entry in A:
        entries.discard(entry)
        low, high = entry - 1, entry + 1
        while low in entries:
            entries.remove(low)
            low -= 1
        while high in entries:
            entries.remove(high)
            high += 1
        longest_range = max(longest_range, high - low - 1)
    return longest_range


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
