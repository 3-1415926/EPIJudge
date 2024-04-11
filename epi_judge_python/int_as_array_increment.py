from typing import List

from test_framework import generic_test

BASE = 10

def plus_one(A: List[int]) -> List[int]:
    carry, i = 1, len(A) - 1
    while carry and i >= 0:
        digit = A[i] + carry
        A[i] = digit % BASE
        carry = digit // BASE
        i -= 1
    if carry and i < 0:
        A.insert(0, carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
