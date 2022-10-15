from typing import List

from test_framework import generic_test


def max_square_submatrix(A: List[List[bool]]) -> int:
    if len(A) == 0: return 0
    N, M = len(A), len(A[0])
    max_side = 0
    prev, cur = [0] * M, [0] * M
    for i in range(N):
        cur[0] = int(A[i][0])
        for j in range(1, M):
            cand_side = min(cur[j - 1], prev[j])
            cur[j] = A[i][j] * (cand_side + A[i - cand_side][j - cand_side])
        max_side = max(max_side, max(cur))
        prev = cur
    return max_side * max_side


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_square_submatrix.py',
                                       'max_square_submatrix.tsv',
                                       max_square_submatrix))
