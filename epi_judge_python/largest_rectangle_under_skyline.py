import collections
from typing import List

from test_framework import generic_test


IndexHeight = collections.namedtuple('IndexHeight', ['index', 'height'])


def calculate_largest_rectangle(heights: List[int]) -> int:
    stack = []
    max_area = 0
    i = 0
    while True:
        start_i = i
        while len(stack) > 0 and stack[-1].height >= (heights[i] if i < len(heights) else 0):
            start_i, prev_height = stack.pop()
            max_area = max(max_area, prev_height * (i - start_i))
        if i >= len(heights): break
        stack.append(IndexHeight(start_i, heights[i]))
        i += 1
    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
