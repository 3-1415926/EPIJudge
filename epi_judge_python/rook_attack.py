import copy
from typing import List

from test_framework import generic_test


def rook_attack(A: List[List[int]]) -> None:
    if not A:
        return
    first_row_has_rooks = any(A[0][c] == 0 for c in range(len(A[0])))
    first_col_has_rooks = any(A[r][0] == 0 for r in range(len(A)))
    for r in range(1, len(A)):
        if any(A[r][c] == 0 for c in range(1, len(A[r]))):
            A[r][0] = 0
    for c in range(1, len(A[0])):
        if any(A[r][c] == 0 for r in range(1, len(A))):
            A[0][c] = 0
    for r in range(1, len(A)):
        for c in range(1, len(A[r])):
            if A[r][0] == 0 or A[0][c] == 0:
                A[r][c] = 0
    if first_row_has_rooks:
        for c in range(len(A[0])):
            A[0][c] = 0
    if first_col_has_rooks:
        for r in range(len(A)):
            A[r][0] = 0


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rook_attack.py', 'rook_attack.tsv',
                                       rook_attack_wrapper))
