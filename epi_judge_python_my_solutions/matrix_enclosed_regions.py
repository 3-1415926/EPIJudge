import traceback
from typing import List

from test_framework import generic_test


DELTA = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def fill_surrounded_regions(board: List[List[str]]) -> None:
    def fill_recursive(r, c):
        if board[r][c] != 'W': return
        board[r][c] = 'T'
        for dr, dc in DELTA:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(board) or not 0 <= nc < len(board[nr]): continue
            fill_recursive(nr, nc)
    for r in range(len(board)):
        fill_recursive(r, 0)
        fill_recursive(r, len(board[r]) - 1)
    for c in range(len(board[0])):
        fill_recursive(0, c)
        fill_recursive(len(board) - 1, c)
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'W': board[r][c] = 'B'
            if board[r][c] == 'T': board[r][c] = 'W'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
