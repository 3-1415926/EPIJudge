import collections
from functools import reduce
from operator import xor
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def last_set_bit(x):
    return x ^ (x & (x - 1))

def calculate_xor_diff(items, predicate=lambda _: True):
    expected = filter(predicate, range(len(items)))
    actual = filter(predicate, items)
    return reduce(xor, expected, 0) ^ reduce(xor, actual, 0)

def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    xor_diff = calculate_xor_diff(A)
    diff_bit = last_set_bit(xor_diff)
    missing = calculate_xor_diff(A, lambda x: x & diff_bit)
    duplicate = calculate_xor_diff(A, lambda x: ~(x | ~diff_bit))
    if missing in A: missing, duplicate = duplicate, missing
    assert missing not in A, f'Missing {missing} is actually present'
    assert sum(x == duplicate for x in A) == 2, f'Duplicate {duplicate} is actually not duplicate'
    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
