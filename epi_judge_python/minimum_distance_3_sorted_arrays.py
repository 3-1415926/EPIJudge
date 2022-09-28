import collections
import heapq
from typing import List

from test_framework import generic_test


HeapEntry = collections.namedtuple('HeapEntry', ['value', 'array_idx', 'idx_in_array'])


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    if not all(len(a) for a in sorted_arrays): raise ValueError('Empty arrays')
    idx_heap = [HeapEntry(sorted_arrays[i][0], i, 0) for i in range(len(sorted_arrays))]
    heapq.heapify(idx_heap)
    max_entry = max(idx_heap)
    min_interval = float('inf')
    while True:
        min_entry = heapq.heappop(idx_heap)
        min_interval = min(min_interval, max_entry.value - min_entry.value)
        next_idx_in_array = min_entry.idx_in_array + 1
        if next_idx_in_array >= len(sorted_arrays[min_entry.array_idx]):
            break
        next_entry = HeapEntry(
            sorted_arrays[min_entry.array_idx][next_idx_in_array],
            min_entry.array_idx, next_idx_in_array)
        max_entry = max(max_entry, next_entry)
        heapq.heappush(idx_heap, next_entry)
    return min_interval


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
