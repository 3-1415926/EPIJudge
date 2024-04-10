from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    left, right = 0, len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] >= k:
            right = mid
        else:
            left = mid + 1
    return left if left < len(A) and A[left] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
