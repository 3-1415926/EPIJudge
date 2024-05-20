from typing import List

from test_framework import generic_test


def binary_search_unknown_length(A: List[int], k: int) -> int:
    left, right = 0, float('inf')
    while left < right:
        mid = (left + 1) * 2 if right == float('inf') else (left + right) // 2
        try:
            if k <= A[mid]:
                right = mid
            else:
                left = mid + 1
        except IndexError:
            right = mid
    return left if left < len(A) and A[left] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_unknown_length_array.py',
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
