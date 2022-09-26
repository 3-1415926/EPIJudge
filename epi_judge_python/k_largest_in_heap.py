import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    result = []
    max_heap = []
    heapq.heappush(max_heap, (-A[0], 0))
    for _ in range(k):
        value, i = heapq.heappop(max_heap)
        result.append(-value)
        left_i, right_i = i * 2 + 1, i * 2 + 2
        if left_i < len(A): heapq.heappush(max_heap, (-A[left_i], left_i))
        if right_i < len(A): heapq.heappush(max_heap, (-A[right_i], right_i))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
