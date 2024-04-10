import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap = []
    max_heap = []
    medians = []
    median = 0
    for item in sequence:
        if item >= median:
            heapq.heappush(min_heap, item)
            if len(min_heap) > len(max_heap) + 1:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        else:
            heapq.heappush(max_heap, -item)
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        median = min_heap[0] if len(min_heap) > len(max_heap) else -max_heap[0] if len(max_heap) > len(min_heap) else (min_heap[0] - max_heap[0]) / 2
        medians.append(median)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
