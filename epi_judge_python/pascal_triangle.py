from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n <= 0: return []
    result = [[1]]
    for i in range(1, n):
        result.append([0] * (i + 1))
        for j in range(i + 1):
            if j - 1 >= 0: result[i][j] += result[i - 1][j - 1]
            if j < i: result[i][j] += result[i - 1][j]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
