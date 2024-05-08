import heapq
from typing import List

from test_framework import generic_test


def sign(x: int) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    slices = []
    running_sign = 0
    from_idx = 0
    for i in range(1, len(A)):
        new_sign = sign(A[i] - A[i - 1])
        if new_sign * running_sign < 0:
            slices.append(slice(from_idx, i, 1) if running_sign >= 0
                          else slice(i - 1, from_idx - 1, -1))
            running_sign = new_sign
            from_idx = i
        else:
            running_sign = sign(running_sign + new_sign)
    slices.append(slice(from_idx, len(A), 1) if running_sign >= 0
                  else slice(len(A) - 1, from_idx - 1, -1))
    heap = []
    for slice_idx in range(len(slices)):
        heapq.heappush(heap, (A[slices[slice_idx].start], slices[slice_idx].start, slice_idx))
    results = []
    while heap:
        value, item_idx, slice_idx = heapq.heappop(heap)
        results.append(value)
        item_idx += slices[slice_idx].step
        if item_idx != slices[slice_idx].stop:
            heapq.heappush(heap, (A[item_idx], item_idx, slice_idx))
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
