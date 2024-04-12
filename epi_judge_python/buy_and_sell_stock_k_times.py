from itertools import chain
from typing import List, Iterable, Tuple

from test_framework import generic_test


def skip_equal(prices: Iterable[float]) -> Iterable[float]:
    last_price = None
    for price in prices:
        if last_price != price:
            last_price = price
            yield price
            

def skip_monotonic(prices: Iterable[float]) -> Iterable[float]:
    last_price, price = None, None
    for next_price in chain(prices, [None]):
        if price is not None:
            if last_price is None or next_price is None or (last_price < price) != (price < next_price):
                yield price
        last_price = price
        price = next_price


def unrestricted_buy_and_sell(prices: List[float]) -> Tuple[int, float]:
    last_price = float('inf')
    k, total_profit = 0, 0.
    for price in prices:
        if price > last_price:
            total_profit += price - last_price
            k += 1            
        last_price = price
    return k, total_profit
        

def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
    unrestricted_k, unrestricted_profit = unrestricted_buy_and_sell(prices)
    if unrestricted_k <= k:
        return unrestricted_profit
    after_buy = [float('-inf')] * k
    after_sell = [float('-inf')] * k
    for price in prices:
        for i in range(k):
            after_buy[i] = max(after_buy[i], (after_sell[i - 1] if i > 0 else 0) - price)
            after_sell[i] = max(after_sell[i], after_buy[i] + price)
    return after_sell[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_k_times.py',
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
