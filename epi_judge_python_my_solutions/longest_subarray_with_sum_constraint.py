from typing import List

from test_framework import generic_test


def find_longest_subarray_less_equal_k(A: List[int], k: int) -> int:
    prefix_sum = [0] + A
    for i in range(1, len(A) + 1):
        prefix_sum[i] += prefix_sum[i - 1]
    min_sum_on_after = prefix_sum.copy()
    for i in range(len(A) - 1, -1, -1):
        min_sum_on_after[i] = min(min_sum_on_after[i], min_sum_on_after[i + 1])
    i, max_len = 0, 0
    for j in range(len(A) + 1):
        if min_sum_on_after[j] - prefix_sum[i] > k: i += 1
        else: max_len = max(max_len, j - i)
    return max_len


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_sum_constraint.py',
            'longest_subarray_with_sum_constraint.tsv',
            find_longest_subarray_less_equal_k))
