from functools import cache
from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    cur, prev = coins.copy(), [0] * (len(coins))
    for d in range(1, len(coins)):
        prev, cur = cur, prev
        for i in range(len(coins) - d):
            j = i + d
            cur[i] = max(coins[i] - prev[i + 1], coins[j] - prev[i])
        del cur[len(coins) - d:]
    return (sum(coins) + cur[0]) // 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
