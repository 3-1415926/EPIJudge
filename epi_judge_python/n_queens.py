from typing import List

from test_framework import generic_test


def n_queens(n: int, col_idx: int = 0, rows: List[bool] = None,
             main_diags: List[bool] = None, anti_diags: List[bool] = None) -> List[List[int]]:
    if col_idx == n: return [[]]
    if rows is None: rows = [False] * n
    if main_diags is None: main_diags = [False] * (2 * n - 1)
    if anti_diags is None: anti_diags = [False] * (2 * n - 1)
    results = []
    for row_idx in range(n):
        main_diag_idx, anti_diag_idx = col_idx - row_idx + n - 1, col_idx + row_idx
        if (not rows[row_idx] and
            not main_diags[main_diag_idx] and
            not anti_diags[anti_diag_idx]):
            rows[row_idx], main_diags[main_diag_idx], anti_diags[anti_diag_idx] = True, True, True
            for remainder in n_queens(n, col_idx + 1, rows, main_diags, anti_diags):
                results.append([row_idx] + remainder)
            rows[row_idx], main_diags[main_diag_idx], anti_diags[anti_diag_idx] = False, False, False
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
