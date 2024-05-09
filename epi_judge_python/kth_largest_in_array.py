from typing import List

from test_framework import generic_test


def pivot(pv: int, A: List[int], left: int, right: int) -> int:
    # Invariant: A[left:i] > pv, A[i:j] == pv, A[j:k] == ?, A[k:right] < pv
    i, j, k = left, left, right
    while j < k:
        if A[j] > pv:
            A[i], A[j] = A[j], A[i]
            i += 1
            j += 1
        elif A[j] < pv:
            k -= 1
            A[j], A[k] = A[k], A[j]
        else:
            j += 1
    return (i + j) // 2


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int], left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(A)
    assert left < right
    assert 1 <= k <= right - left
    while left + 1 < right:
        mid = pivot(A[(left + right) // 2], A, left, right)
        if k <= mid - left:
            right = mid
        else:
            k -= mid - left
            left = mid
    assert k == 1
    return A[left]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
