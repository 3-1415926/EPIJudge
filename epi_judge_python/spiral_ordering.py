from itertools import chain
from typing import List

from test_framework import generic_test


class IterateHelper:
    def __init__(self, matrix):
        self._matrix = matrix
        self._n = len(matrix)

    def set_length(self, length):
        self._length = length

    def iterate(self, r, c, *, dr=0, dc=0):
        if r < 0: r += self._n
        if c < 0: c += self._n
        for _ in range(self._length):
            yield self._matrix[r][c]
            r += dr
            c += dc


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(square_matrix)
    it = IterateHelper(square_matrix)
    for k in range(n // 2):
        it.set_length(n - k * 2 - 1)
        for x in chain(it.iterate( k,  k, dc= 1),
                       it.iterate( k, ~k, dr= 1),
                       it.iterate(~k, ~k, dc=-1),
                       it.iterate(~k,  k, dr=-1)):
            result.append(x)
    if n % 2 != 0:
        result.append(square_matrix[n // 2][n // 2])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
