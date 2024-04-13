from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(square_matrix)
    for offset in range(n):
        rng = range(offset, n - offset - 1)
        for i in rng: result.append(square_matrix[offset][i])
        for i in rng: result.append(square_matrix[i][~offset])
        for i in rng: result.append(square_matrix[~offset][~i])
        for i in rng: result.append(square_matrix[~i][offset])
    if n % 2 != 0:
        result.append(square_matrix[n // 2][n // 2])
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
