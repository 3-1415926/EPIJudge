from typing import List

from test_framework import generic_test


def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
    if 2 * k >= len(prices):
        return sum(max(0, b - a) for a, b in zip(prices[:-1], prices[1:]))
    after_buy =  [None] + [float('-inf')] * k
    after_sell = [0]    + [float('-inf')] * k
    for p in prices:
        for k in range(1, k + 1):
            after_buy [k] = max(after_buy [k], after_sell[k - 1] - p)
            after_sell[k] = max(after_sell[k], after_buy [k]     + p)
    return after_sell[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_k_times.py',
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
