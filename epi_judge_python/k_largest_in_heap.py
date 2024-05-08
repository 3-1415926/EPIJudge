import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k == 0: return []
    results = []
    heap = [(~A[0], 0)]
    for _ in range(k):
        value, idx = heapq.heappop(heap)
        results.append(~value)
        for child_idx in [idx * 2 + 1, idx * 2 + 2]:
            if child_idx < len(A):
                heapq.heappush(heap, (~A[child_idx], child_idx))
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
