from typing import List

from test_framework import generic_test


def calculate_bonus(productivity: List[int]) -> int:
    tickets = [1] * len(productivity)
    for i in range(1, len(productivity)):
        if productivity[i - 1] < productivity[i]:
            tickets[i] = max(tickets[i], tickets[i - 1] + 1)
    for i in range(len(productivity) - 2, -1, -1):
        if productivity[i] > productivity[i + 1]:
            tickets[i] = max(tickets[i], tickets[i + 1] + 1)
    return sum(tickets)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bonus.py', 'bonus.tsv',
                                       calculate_bonus))
