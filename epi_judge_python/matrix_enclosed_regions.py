from typing import List

from test_framework import generic_test

DX, DY = [-1, 0, 1, 0], [0, 1, 0, -1]
W, B, T = "W", "B", "T"

def fill(board: List[List[str]], x: int, y: int, new_color: str):
    old_color = board[x][y]
    board[x][y] = new_color
    for dx, dy in zip(DX, DY):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[nx]) and board[nx][ny] == old_color:
            fill(board, nx, ny, new_color)

def fill_surrounded_regions(board: List[List[str]]) -> None:
    for x in range(len(board)):
        for y in [0, len(board[x]) - 1]:
            if board[x][y] == W:
                fill(board, x, y, T)
    for x in [0, len(board) - 1]:
        for y in range(len(board[x])):
            if board[x][y] == W:
                fill(board, x, y, T)
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == W:
                board[x][y] = B
            elif board[x][y] == T:
                board[x][y] = W


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
