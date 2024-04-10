from typing import List

from test_framework import generic_test


def calculate_trapping_water(heights: List[int]) -> int:
    if not heights: return 0
    total_water = 0
    max_lh, max_rh = 0, 0
    l, r = 0, len(heights) - 1
    while l < r:
        if heights[l] < heights[r]:
            if max_lh > heights[l]:
                total_water += max_lh - heights[l]
            else:
                max_lh = heights[l]
            l += 1
        else:
            if max_rh > heights[r]:
                total_water += max_rh - heights[r]
            else:
                max_rh = heights[r]
            r -= 1
    assert l == r
    total_water += max(0, min(max_lh, max_rh) - heights[l])
    return total_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_water_trappable.py',
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
