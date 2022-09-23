from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    cur_min = float('inf')
    max_profit = 0.
    for p in prices:
        if cur_min > p:
            cur_min = p
        if max_profit < p - cur_min:
            max_profit = p - cur_min
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
