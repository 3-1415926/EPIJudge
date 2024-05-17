import heapq
import math
from typing import List, NamedTuple

from test_framework import generic_test

SQRT2 = math.sqrt(2)

class HeapEntry(NamedTuple):
    value: float
    x: int
    y: int
    
    @staticmethod
    def make(x: int, y: int) -> "HeapEntry":
        return HeapEntry(x + y * SQRT2, x, y)


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    results = []
    heap = [HeapEntry.make(0, 0)]
    while len(results) < k:
        cur_min = heapq.heappop(heap)
        if results and math.isclose(results[-1], cur_min.value):
            continue
        results.append(cur_min.value)
        heapq.heappush(heap, HeapEntry.make(cur_min.x, cur_min.y + 1))
        heapq.heappush(heap, HeapEntry.make(cur_min.x + 1, cur_min.y))
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
