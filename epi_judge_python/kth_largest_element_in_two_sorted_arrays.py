from typing import List

from test_framework import generic_test


def find_kth_in_two_sorted_arrays(A: List[int], B: List[int], k: int) -> int:
    def to_B_index(A_index: int):
        return k - A_index
    if not (0 < k <= len(A) + len(B)): raise ValueError()
    A_left, A_right = max(0, k - len(B)), min(k, len(A))
    while A_left < A_right:
        A_mid = (A_left + A_right) // 2
        B_mid = to_B_index(A_mid) - 1
        if B_mid >= len(B) or A[A_mid] < B[B_mid]:
            A_left = A_mid + 1
        else:
            A_right = A_mid
    B_left = to_B_index(A_left)
    return max(A[A_left - 1] if A_left > 0 else float('-inf'), B[B_left - 1] if B_left > 0 else float('-inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'kth_largest_element_in_two_sorted_arrays.py',
            'kth_largest_element_in_two_sorted_arrays.tsv',
            find_kth_in_two_sorted_arrays))
