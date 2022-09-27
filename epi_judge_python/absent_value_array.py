import itertools
from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int], base:int = 10) -> int:
    iters = itertools.tee(stream, 3)
    result = 0
    buck = None
    for i in range(len(iters)):
        buckets = [0] * base
        for item in iters[i]:
            if item % base ** i == result:
                buckets[item % base ** (i + 1) // base ** i] += 1
        buck = min(range(len(buckets)), key=lambda i: buckets[i])
        result += buck * base ** i
    return result


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
