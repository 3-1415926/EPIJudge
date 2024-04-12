from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price = float('inf')
    best_profit = 0.
    for price in prices:
        best_profit = max(best_profit, price - min_price)
        min_price = min(min_price, price)
    return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
