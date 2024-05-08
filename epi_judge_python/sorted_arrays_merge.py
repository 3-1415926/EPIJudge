import heapq
from typing import List, NamedTuple

from test_framework import generic_test


class ArrayItem(NamedTuple):
    value: int
    item_idx: int
    array_idx: int


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = []
    for array_idx in range(len(sorted_arrays)):
        if sorted_arrays[array_idx]:
            heapq.heappush(heap, ArrayItem(sorted_arrays[array_idx][0],
                                           item_idx=0, array_idx=array_idx))
    result = []
    while heap:
        item = heapq.heappop(heap)
        result.append(item.value)
        if item.item_idx + 1 < len(sorted_arrays[item.array_idx]):
            heapq.heappush(heap, ArrayItem(sorted_arrays[item.array_idx][item.item_idx + 1],
                                           item_idx=item.item_idx + 1,
                                           array_idx=item.array_idx))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
