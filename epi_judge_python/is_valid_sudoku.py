from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    N = 3
    NN = N * N
    rows, cols, sqrs = [0] * NN, [0] * NN, [0] * NN
    for r in range(len(partial_assignment)):
        for c in range(len(partial_assignment[r])):
            digit = partial_assignment[r][c]
            if digit == 0: continue
            mask = 1 << digit
            if rows[r] & mask: return False
            rows[r] |= mask
            if cols[c] & mask: return False
            cols[c] |= mask
            sqr_idx = r // N * N + c // N
            if sqrs[sqr_idx] & mask: return False
            sqrs[sqr_idx] |= mask
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
