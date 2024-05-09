import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    assert A
    smallest, largest = float('inf'), float('-inf')
    for i in range(0, len(A), 2):
        j = min(i + 1, len(A) - 1)
        mi, ma = (A[i], A[j]) if A[i] <= A[j] else (A[j], A[i])
        if largest < ma:
            largest = ma
        if smallest > mi:
            smallest = mi
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
