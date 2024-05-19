from typing import List

from test_framework import generic_test


DX, DY = [-1, 0, 1, 0], [0, 1, 0, -1]


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    old_color = image[x][y]
    image[x][y] = not old_color
    for dx, dy in zip(DX, DY):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(image) and 0 <= ny < len(image[nx]) and image[nx][ny] == old_color:
            flip_color(nx, ny, image)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
