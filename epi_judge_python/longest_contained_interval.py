from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    longest = 0
    items = set(A)
    while len(items) > 0:
        item = items.pop()
        upper = item
        while upper + 1 in items:
            upper += 1
            items.remove(upper)
        lower = item
        while lower - 1 in items:
            lower -= 1
            items.remove(lower)
        longest = max(longest, upper - lower + 1)
    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
