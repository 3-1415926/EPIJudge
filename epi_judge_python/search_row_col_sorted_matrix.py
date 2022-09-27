from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    if len(A) == 0 or len(A[0]) == 0: return False
    i = 0
    j = len(A[0]) - 1
    while A[i][j] != x:
        if A[i][j] > x:
            j -= 1
            if j < 0: return False
        else:
            i += 1
            if i >= len(A): return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
