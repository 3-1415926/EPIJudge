import functools
from typing import List

from test_framework import generic_test

def maximum_revenue(coins: List[int]) -> int:
    @functools.cache
    def recursive_revenue(start: int, end: int, total: int):
        if end <= start: return 0
        if end == start + 1: return coins[start]
        return total - min(recursive_revenue(start + 1, end, total - coins[start]),
                           recursive_revenue(start, end - 1, total - coins[end - 1]))
    return recursive_revenue(0, len(coins), sum(coins))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
