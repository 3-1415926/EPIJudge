import heapq
from typing import List, NamedTuple

from test_framework import generic_test

class HeapEntry(NamedTuple):
    value: int
    arr_idx: int
    idx_in_arr: int


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    def make_entry(arr_idx: int, idx_in_arr: int) -> HeapEntry:
        return HeapEntry(sorted_arrays[arr_idx][idx_in_arr], arr_idx, idx_in_arr)
    if not all(sorted_arrays):
        return -1
    min_diff = float('inf')
    heap = [make_entry(i, 0) for i in range(len(sorted_arrays))]
    heapq.heapify(heap)
    max_entry = max(heap)
    while True:
        min_entry = heapq.heappop(heap)
        min_diff = min(min_diff, max_entry.value - min_entry.value)
        if min_entry.idx_in_arr + 1 >= len(sorted_arrays[min_entry.arr_idx]):
            break
        new_entry = make_entry(min_entry.arr_idx, min_entry.idx_in_arr + 1)
        max_entry = max(max_entry, new_entry)
        heapq.heappush(heap, new_entry)
    return min_diff


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
