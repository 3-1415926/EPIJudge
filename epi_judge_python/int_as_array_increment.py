from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    carry = 1
    while i >= 0 and carry != 0:
        A[i] += carry
        carry, A[i] = A[i] // 10, A[i] % 10
        i -= 1
    if carry != 0:
        A.insert(0, carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
