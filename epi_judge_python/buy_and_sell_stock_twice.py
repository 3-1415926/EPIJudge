from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    after_buy1, after_sell1, after_buy2, after_sell2 = [float('-inf')] * 4
    for p in prices:
        after_buy1 =  max(after_buy1,              - p)
        after_sell1 = max(after_sell1, after_buy1  + p)
        after_buy2 =  max(after_buy2,  after_sell1 - p)
        after_sell2 = max(after_sell2, after_buy2  + p)
    return after_sell2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
