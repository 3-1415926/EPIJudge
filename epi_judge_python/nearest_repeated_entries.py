from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    last_positions = {}
    min_dist = float('inf')
    for i in range(len(paragraph)):
        last_pos = last_positions.get(paragraph[i], float('-inf'))
        min_dist = min(min_dist, i - last_pos)
        last_positions[paragraph[i]] = i
    return min_dist if min_dist < float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
