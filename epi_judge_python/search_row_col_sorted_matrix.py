from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    r, c = len(A) - 1, 0
    while r >= 0 and c < len(A[r]):
        if A[r][c] < x:
            c += 1
        elif A[r][c] > x:
            r -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
