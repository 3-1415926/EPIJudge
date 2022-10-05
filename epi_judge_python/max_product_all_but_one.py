from functools import reduce
from operator import mul
from typing import Iterable, List

from test_framework import generic_test


def find_biggest_n_minus_one_product(A: List[int]) -> int:
    num_negative = sum(a < 0 for a in A)
    if num_negative == len(A) or num_negative % 2 == 1:
        max_negative_idx = max((i for i in range(len(A)) if A[i] < 0), key=lambda i: A[i])
        return reduce(mul, (A[i] for i in range(len(A)) if i != max_negative_idx), 1)
    else:
        min_nonnegative_idx = min((i for i in range(len(A)) if A[i] >= 0), key=lambda i: A[i])
        return reduce(mul, (A[i] for i in range(len(A)) if i != min_nonnegative_idx), 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_product_all_but_one.py',
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
