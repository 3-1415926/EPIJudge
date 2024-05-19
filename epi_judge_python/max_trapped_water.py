from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    max_left, max_right = float('-inf'), float('-inf')
    max_trapped = 0
    while left < right:
        max_left = max(max_left, heights[left])
        max_right = max(max_right, heights[right])
        max_trapped = max(max_trapped, min(max_left, max_right) * (right - left))
        if max_left <= max_right:
            left += 1
        else:
            right -= 1
    return max_trapped


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
