from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)
    for k in range(n // 2):
        for i in range(k, n - k - 1):
            temp =                  square_matrix[ k][ i]
            square_matrix[ k][ i] = square_matrix[~i][ k]
            square_matrix[~i][ k] = square_matrix[~k][~i]
            square_matrix[~k][~i] = square_matrix[ i][~k]
            square_matrix[ i][~k] = temp


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
