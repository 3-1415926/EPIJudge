import bisect
from typing import List

from test_framework import generic_test

def h_index(citations: List[int]) -> int:
    citations.sort(reverse=True)
    # left, right = 0, len(citations)
    # while left < right:
    #     mid = (left + right) // 2
    #     if citations[mid] > mid:
    #         left = mid + 1
    #     else:
    #         right = mid
    # return left
    return bisect.bisect_left(range(len(citations)), 0, key=lambda i: i - citations[i])


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
