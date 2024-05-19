from itertools import chain
from typing import List, Iterable, Tuple

from test_framework import generic_test


def unrestricted_buy_and_sell(prices: List[float]) -> Tuple[float, int]:
    if not prices:
        return 0, 0
    profit, k = 0, 0
    local_min, local_max = prices[0], prices[0]
    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:
            if local_max > local_min:
                profit += local_max - local_min
                k += 1
            local_min = local_max = prices[i]
        elif prices[i] > prices[i - 1]:
            local_max = prices[i]
    if local_max > local_min:
        profit += local_max - local_min
        k += 1
    return profit, k


def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
    unrestricted_profit, unrestricted_k = unrestricted_buy_and_sell(prices)
    if unrestricted_k <= k:
        return unrestricted_profit
    after_buy, after_sell = [float('-inf')] * k, [float('-inf')] * k
    for p in prices:
        for i in range(k):
            after_buy[i] = max(after_buy[i], (after_sell[i - 1] if i > 0 else 0) - p)
            after_sell[i] = max(after_sell[i], after_buy[i] + p)
    return after_sell[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_k_times.py',
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
