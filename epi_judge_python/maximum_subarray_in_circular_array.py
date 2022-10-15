from typing import List

from test_framework import generic_test


def extremum_subarray_sum(A: List[int], fn) -> int:
    extremum_sum = None
    extremum_sum_up_to = None
    for a in A:
        extremum_sum_up_to = a if extremum_sum_up_to is None else fn(a, extremum_sum_up_to + a)
        extremum_sum = extremum_sum_up_to if extremum_sum is None else fn(extremum_sum_up_to, extremum_sum)
    return extremum_sum

def max_subarray_sum_in_circular(A: List[int]) -> int:
    return max(extremum_subarray_sum(A, max), sum(A) - extremum_subarray_sum(A, min))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'maximum_subarray_in_circular_array.py',
            'maximum_subarray_in_circular_array.tsv',
            max_subarray_sum_in_circular))
