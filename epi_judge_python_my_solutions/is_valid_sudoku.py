import math
from typing import List

from test_framework import generic_test

def is_valid(partial_assignment, row_slice, col_slice):
    if type(row_slice) is int: row_slice = slice(row_slice, row_slice + 1)
    if type(col_slice) is int: col_slice = slice(col_slice, col_slice + 1)
    N = len(partial_assignment)
    bits = [False] * N
    for i in range(row_slice.start or 0, row_slice.stop, row_slice.step or 1):
        for j in range(col_slice.start or 0, col_slice.stop, col_slice.step or 1):
            if partial_assignment[i][j] == 0:
                continue
            if not 1 <= partial_assignment[i][j] <= N:
                return False
            if bits[partial_assignment[i][j] - 1]:
                return False
            bits[partial_assignment[i][j] - 1] = True
    return True


def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    N = len(partial_assignment)
    sqrtN = round(math.sqrt(N))
    assert sqrtN * sqrtN == N

    for i in range(N):
        if not is_valid(partial_assignment, i, slice(N)): return False
        if not is_valid(partial_assignment, slice(N), i): return False
        if not is_valid(partial_assignment,
                        slice(i // sqrtN * sqrtN, (i // sqrtN + 1) * sqrtN),
                        slice(i % sqrtN * sqrtN,  (i % sqrtN + 1) * sqrtN)): return False

    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
