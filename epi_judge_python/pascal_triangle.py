from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n <= 0:
        return []
    rows = [[1]]
    for r in range(2, n + 1):
        row = []
        for c in range(r):
            row.append((rows[-1][c - 1] if c > 0 else 0) + (rows[-1][c] if c < r - 1 else 0))
        rows.append(row)
    return rows


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
