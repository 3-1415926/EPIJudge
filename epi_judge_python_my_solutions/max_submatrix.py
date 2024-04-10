from typing import List

from test_framework import generic_test

def max_rectangle_submatrix(A: List[List[bool]]) -> int:
    if len(A) == 0: return 0
    N, M = len(A), len(A[0])
    result = 0
    heights = [0] * M
    for i in range(N):
        stack = []
        for j in range(M):
            heights[j] = heights[j] + 1 if A[i][j] else 0
            start_j = j
            while stack and stack[-1][1] > heights[j]:
                start_j, height = stack.pop()
                result = max(result, (j - start_j) * height)
            stack.append((start_j, heights[j]))
        while stack:
            start_j, height = stack.pop()
            result = max(result, (M - start_j) * height)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_submatrix.py', 'max_submatrix.tsv',
                                       max_rectangle_submatrix))
