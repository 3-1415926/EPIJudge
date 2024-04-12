from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    last_reachable = 0
    for i in range(len(A)):
        if i > last_reachable:
            return False
        last_reachable = max(last_reachable, i + A[i])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
