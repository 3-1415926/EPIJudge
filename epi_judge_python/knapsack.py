import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    best_values = {0: 0.}
    for item in items:
        for w in sorted(best_values, reverse=True):
            new_weight = w + item.weight
            if new_weight <= capacity and (new_weight not in best_values or best_values[new_weight] < best_values[w] + item.value):
                best_values[new_weight] = best_values[w] + item.value
    return max(best_values.values())


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
