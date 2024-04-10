import heapq
from typing import List

from test_framework import generic_test


def reverse(A: List[int], left: int, right: int):
    for i in range((right - left) // 2):
        A[left + i], A[right + ~i] = A[right + ~i], A[left + i]


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if len(A) <= 1: return A
    increasing = None
    boundaries = [0]
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            continue
        if increasing is not None and increasing != (A[i] > A[i - 1]):
            if not increasing:
                reverse(A, boundaries[-1], i)
            boundaries.append(i)
        increasing = A[i] > A[i - 1]
    if not increasing:
        reverse(A, boundaries[-1], len(A))
    boundaries.append(len(A))
    min_heap = []
    result = []
    indices = boundaries[:-1]
    for i in range(len(indices)):
        if indices[i] < boundaries[i + 1]:
            heapq.heappush(min_heap, (A[indices[i]], i))
            indices[i] += 1
    while len(min_heap) > 0:
        smallest, i = heapq.heappop(min_heap)
        result.append(smallest)
        if indices[i] < boundaries[i + 1]:
            heapq.heappush(min_heap, (A[indices[i]], i))
            indices[i] += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
