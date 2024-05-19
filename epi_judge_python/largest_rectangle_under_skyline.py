from typing import List, NamedTuple

from test_framework import generic_test


class StackEntry(NamedTuple):
    x: int
    y: int


def calculate_largest_rectangle(heights: List[int]) -> int:
    max_area = 0
    stack = []
    for i in range(len(heights)):
        x = None
        while stack and stack[-1].y > heights[i]:
            x, y = stack.pop()
            max_area = max(max_area, y * (i - x))
        stack.append(StackEntry(x if x is not None else i, heights[i]))
    while stack:
        x, y = stack.pop()
        max_area = max(max_area, y * (len(heights) - x))
    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
