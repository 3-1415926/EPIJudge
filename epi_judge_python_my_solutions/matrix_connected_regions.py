from typing import List, Optional

from test_framework import generic_test

DELTA = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def flip_color(x: int, y: int, image: List[List[bool]], matching_color: Optional[bool] = None) -> None:
    if matching_color is None: matching_color = image[x][y]
    assert matching_color == image[x][y]
    image[x][y] = not matching_color
    for dx, dy in DELTA:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < len(image) or not 0 <= ny < len(image[nx]): continue
        if image[nx][ny] == matching_color:
            flip_color(nx, ny, image, matching_color)

    


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
