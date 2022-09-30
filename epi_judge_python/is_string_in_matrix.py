from typing import List

from test_framework import generic_test

DELTA = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    if not pattern: return True
    prev_cont = [[None] * len(grid[i]) for i in range(len(grid))]
    cont = [[grid[i][j] == pattern[0] for j in range(len(grid[i]))] for i in range(len(grid))]
    for p in range(1, len(pattern)):
        prev_cont, cont = cont, prev_cont
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != pattern[p]:
                    cont[i][j] = False
                    continue
                for di, dj in DELTA:
                    if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i]) and prev_cont[i + di][j + dj]:
                        cont[i][j] = True
                        break
                else:
                    cont[i][j] = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if cont[i][j]: return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
