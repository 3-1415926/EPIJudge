from typing import List

from test_framework import generic_test


def product(A: List[int], skip: int) -> int:
    skipped = False
    product = 1
    for a in A:
        if a == skip and not skipped:
            skipped = True
            continue
        product *= a
    return product


def find_biggest_n_minus_one_product(A: List[int]) -> int:
    num_zeros, num_negative = 0, 0
    max_negative, min_positive = float('-inf'), float('inf')
    for a in A:
        if a < 0:
            num_negative += 1
            max_negative = max(max_negative, a)
        elif a > 0:
            min_positive = min(min_positive, a)
        else:
            num_zeros += 1        
    if num_zeros > 1:
        return 0
    if num_zeros == 1:
        return product(A, 0) if num_negative % 2 == 0 else 0
    return product(A, max_negative if num_negative % 2 != 0 else min_positive)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_product_all_but_one.py',
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
