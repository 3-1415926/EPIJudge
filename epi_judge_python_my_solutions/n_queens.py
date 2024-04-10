from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def place_queens(j: int):
        if j == n:
            results.append(col_placement.copy())
            return
        for i in range(0, n):
            if taken_rows[i] or taken_diagonals[i + j] or taken_anti_diagonals[i - j + n - 1]: continue
            col_placement[j] = i
            taken_rows[i] = taken_diagonals[i + j] = taken_anti_diagonals[i - j + n - 1] = True
            place_queens(j + 1)
            taken_rows[i] = taken_diagonals[i + j] = taken_anti_diagonals[i - j + n - 1] = False
            col_placement[j] = None
    results = []
    col_placement = [None] * n
    taken_rows = [False] * n
    taken_diagonals = [False] * (2 * n - 1)
    taken_anti_diagonals = [False] * (2 * n - 1)
    place_queens(0)
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
