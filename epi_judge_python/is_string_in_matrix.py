from typing import List

from test_framework import generic_test

DR, DC = [0, -1, 0, 1], [1, 0, -1, 0]


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    if not pattern:
        return False
    prev, cur = [[False] * len(r) for r in grid], [[False] * len(r) for r in grid]
    for i in range(len(pattern)):
        prev, cur = cur, prev
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                cur[r][c] = False
                if grid[r][c] != pattern[i]:
                    continue
                if i == 0:
                    cur[r][c] = True
                    continue
                for dr, dc in zip(DR, DC):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                        cur[r][c] |= prev[nr][nc]
    return any(any(r) for r in cur)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
