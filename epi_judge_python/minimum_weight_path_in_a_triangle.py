from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0
    min_path = [float('inf')] * len(triangle)
    min_path[0] = triangle[0][0]
    for i in range(1, len(triangle)):
        min_path[i] = min_path[i - 1] + triangle[i][i]
        for j in reversed(range(1, i)):
            min_path[j] = min(min_path[j], min_path[j - 1]) + triangle[i][j]
        min_path[0] += triangle[i][0]
    return min(min_path)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
