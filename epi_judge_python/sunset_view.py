from typing import Iterator, List
from collections import namedtuple
from test_framework import generic_test


Building = namedtuple('Building', 'idx, height')


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    result = []
    for i in range(len(sequence)):
        while len(result) > 0 and result[-1].height <= sequence[i]:
            result.pop()
        result.append(Building(i, sequence[i]))
    result.reverse()
    return list(map(lambda b: b.idx, result))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
