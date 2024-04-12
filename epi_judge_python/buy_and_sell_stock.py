from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    after_buy, after_sell = [float('-inf')] * 2
    for price in prices:
        after_buy = max(after_buy, 0 - price)
        after_sell = max(after_sell, after_buy + price)
    return after_sell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
