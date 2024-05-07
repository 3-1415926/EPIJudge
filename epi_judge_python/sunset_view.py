from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    heights = []
    indices = []
    for index, height in enumerate(sequence):
        while heights and heights[-1] <= height:
            heights.pop()
            indices.pop()
        heights.append(height)
        indices.append(index)
    indices.reverse()
    return indices


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
