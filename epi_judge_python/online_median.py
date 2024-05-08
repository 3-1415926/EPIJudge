import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    lower_heap = []
    upper_heap = []
    medians = []
    for item in sequence:
        if not upper_heap or item >= upper_heap[0]:
            heapq.heappush(upper_heap, item)
            while len(upper_heap) > len(lower_heap) + 1:
                heapq.heappush(lower_heap, ~heapq.heappop(upper_heap))
        else:
            heapq.heappush(lower_heap, ~item)            
            while len(lower_heap) > len(upper_heap):
                heapq.heappush(upper_heap, ~heapq.heappop(lower_heap))
        medians.append(upper_heap[0] if len(upper_heap) > len(lower_heap)
                       else (upper_heap[0] + ~lower_heap[0]) / 2)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
