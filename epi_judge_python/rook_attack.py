import copy
from typing import List

from test_framework import generic_test


def rook_attack(A: List[List[int]]) -> None:
    if len(A) == 0: return
    rows, cols = len(A), len(A[0])
    first_row_zero = any(not A[0][c] for c in range(cols))
    first_col_zero = any(not A[r][0] for r in range(rows))
    for r in range(1, rows):
        for c in range(1, cols):
            if not A[r][c]:
                A[r][0] = A[0][c] = 0
    for r in range(1, rows):
        if not A[r][0]:
            for c in range(1, cols):
                A[r][c] = 0
    for c in range(1, cols):
        if not A[0][c]:
            for r in range(1, rows):
                A[r][c] = 0
    if first_row_zero:
        for c in range(cols):
            A[0][c] = 0
    if first_col_zero:
        for r in range(rows):
            A[r][0] = 0


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rook_attack.py', 'rook_attack.tsv',
                                       rook_attack_wrapper))
