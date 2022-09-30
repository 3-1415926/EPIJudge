from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    if len(triangle) == 0: return 0
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row - 1][col - 1] if col > 0 else float('inf'),
                                      triangle[row - 1][col] if col < len(triangle[row - 1]) else float('inf'))
    return min(triangle[-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
