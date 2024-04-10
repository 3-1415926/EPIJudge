from typing import List

from test_framework import generic_test


def binary_search_unknown_length(A: List[int], k: int) -> int:
    left, right = 0, None
    while right is None or left < right:
        med = ((left << 1) + 1) if right is None else (left + right) // 2
        try:
            if A[med] < k:
                left = med + 1
                continue
        except IndexError: pass
        right = med
    try:
        if A[left] == k: return left
    except IndexError: pass
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_unknown_length_array.py',
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
