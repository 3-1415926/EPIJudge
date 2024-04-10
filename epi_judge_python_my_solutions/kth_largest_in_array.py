from typing import List, Tuple

from test_framework import generic_test


def pivot_list(pivot: int, A: List[int], left: int = 0, right: int = None) -> Tuple[int, int]:
    if right is None: right = len(A)
    gt = eq = left
    lt = right
    # Invariant: greater [:gt], equal [gt:eq], unknown [eq:lt], less [lt:]
    while eq < lt:
        if A[eq] > pivot:
            A[gt], A[eq] = A[eq], A[gt]
            gt += 1
            eq += 1
        elif A[eq] < pivot:
            lt -= 1
            A[eq], A[lt] = A[lt], A[eq]
        else:
            eq += 1
    return gt, lt



# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int], left: int = 0, right: int = None) -> int:
    k -= 1
    if k >= len(A): return None
    if right is None: right = len(A)
    while left < right:
        pivot = A[(left + right) // 2]
        gt, lt = pivot_list(pivot, A, left, right)
        if k < gt:
            right = gt
        elif k >= lt:
            left = lt
        else: return A[gt]
    return A[left]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
