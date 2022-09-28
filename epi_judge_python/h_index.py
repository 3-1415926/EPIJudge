import bisect
from typing import List

from test_framework import generic_test

def h_index(citations: List[int]) -> int:
    citations.sort()
    # left, right = 0, len(citations)
    # while left < right:
    #     mid = (left + right) // 2
    #     if citations[mid] >= len(citations) - mid:
    #         right = mid
    #     else:
    #         left = mid + 1
    left = bisect.bisect_left(range(len(citations)), 0, key=lambda i: citations[i] - len(citations) + i)
    return min(citations[left], len(citations) - left) if left < len(citations) else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
