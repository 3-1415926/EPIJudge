from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    last_indices = {}
    min_distance = float('inf')
    for i in range(len(paragraph)):
        last_index = last_indices.get(paragraph[i])
        if last_index is not None and (i - last_index < min_distance):
            min_distance = i - last_index
        last_indices[paragraph[i]] = i
    return min_distance if min_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
