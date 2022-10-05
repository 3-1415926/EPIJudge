import heapq
from typing import Iterator

from test_framework import generic_test

def trim_partition(buffer, k):
    start, end = 0, len(buffer)
    while start < end:
        pivot = buffer[(start + end) // 2]
        # Invariant: [:gt] greater, [gt:eq] equal, [eq:ls] unknown, [ls:] less
        gt, eq, lt = start, start, end
        while eq < lt:
            if buffer[eq] > pivot:
                buffer[eq], buffer[gt] = buffer[gt], buffer[eq]
                gt += 1
                eq += 1
            elif buffer[eq] < pivot:
                lt -= 1
                buffer[eq], buffer[lt] = buffer[lt], buffer[eq]
            else:
                eq += 1
        if k < gt - start:
            end = gt
        elif k >= lt - start:
            k -= lt - start
            start = lt
        else:
            break
    del buffer[k + start:]


def find_kth_largest_unknown_length(stream: Iterator[int], k: int) -> int:
    buffer_len = 2 * k
    buffer = []
    for item in stream:
        buffer.append(item)
        if len(buffer) >= buffer_len:
            trim_partition(buffer, k)
    trim_partition(buffer, k)
    return min(buffer)


# Pythonic solution that uses library method but costs O(nlogk) time.
def find_kth_largest_unknown_length_pythonic(stream, k):
    return heapq.nlargest(k, stream)[-1]


def find_kth_largest_unknown_length_wrapper(stream, k):
    return find_kth_largest_unknown_length(iter(stream), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'kth_largest_element_in_long_array.py',
            'kth_largest_element_in_long_array.tsv',
            find_kth_largest_unknown_length_wrapper))
