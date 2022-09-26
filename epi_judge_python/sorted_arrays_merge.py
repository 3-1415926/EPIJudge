import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result = []
    min_heap = []
    iterators = [iter(arr) for arr in sorted_arrays]
    for i in range(len(iterators)):
        element = next(iterators[i], None)
        if element is not None:
            heapq.heappush(min_heap, (element, i))
    while len(min_heap) > 0:
        smallest, i = heapq.heappop(min_heap)
        result.append(smallest)
        element = next(iterators[i], None)
        if element is not None:
            heapq.heappush(min_heap, (element, i))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
