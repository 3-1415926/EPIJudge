import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    def update_min_max(a: int, b: int):
        nonlocal smallest, largest
        if a > b: a, b = b, a
        if a < smallest: smallest = a
        if b > largest: largest = b
    smallest, largest = float('inf'), float('-inf')
    for i in range(len(A) // 2):
        update_min_max(A[i * 2], A[i * 2 + 1])
    if len(A) % 2 == 1:
        update_min_max(A[-1], A[-1])
    return MinMax(smallest, largest)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
