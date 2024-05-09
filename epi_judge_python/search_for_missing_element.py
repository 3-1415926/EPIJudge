import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    miss_xor_dup = functools.reduce(int.__xor__, A) ^ functools.reduce(int.__xor__, range(len(A)))
    bit = miss_xor_dup & ~(miss_xor_dup - 1)
    a = 0
    for item in A:
        if item & bit != 0:
            a ^= item
    for item in range(len(A)):
        if item & bit != 0:
            a ^= item
    b = a ^ miss_xor_dup
    return DuplicateAndMissing(a, b) if a in A else DuplicateAndMissing(b, a)

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
