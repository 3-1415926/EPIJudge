from itertools import product
from math import prod
from typing import List

from test_framework import generic_test


def calculate_bonus(productivity: List[int]) -> int:
    bonus = [1] * len(productivity)
    for i in range(1, len(productivity)):
        if productivity[i] > productivity[i - 1]:
            bonus[i] = max(bonus[i], bonus[i - 1] + 1)
    for i in reversed(range(1, len(productivity))):
        if productivity[i - 1] > productivity[i]:
            bonus[i - 1] = max(bonus[i - 1], bonus[i] + 1)
    return sum(bonus)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bonus.py', 'bonus.tsv',
                                       calculate_bonus))
