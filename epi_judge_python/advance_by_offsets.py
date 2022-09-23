from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_index = 0
    for i in range(len(A)):
        if max_index < i:
            return False
        if max_index < i + A[i]:
            max_index = i + A[i]
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
