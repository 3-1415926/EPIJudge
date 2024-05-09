from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int]) -> int:
    BITS_IN_BYTE = 8
    BYTE_RANGE = 1 << BITS_IN_BYTE
    NUM_BYTES = 4
    counts_by_byte = [[0] * BYTE_RANGE for _ in range(NUM_BYTES)]
    for item in stream:
        for i in range(NUM_BYTES):
            counts_by_byte[i][(item & ((BYTE_RANGE - 1) << (i * BITS_IN_BYTE))) >> (i * BITS_IN_BYTE)] += 1
    result = 0
    for i in reversed(range(NUM_BYTES)):
        byte = min(range(BYTE_RANGE), key=lambda j: counts_by_byte[i][j])
        result = (result << BITS_IN_BYTE) | byte
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
