import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    opt = collections.defaultdict(int)  # weight: value
    opt[0] = 0
    weights = {0}
    for item in items:
        for w in sorted(weights, reverse=True):
            new_weight = item.weight + w
            if new_weight <= capacity and (new_weight not in opt or opt[new_weight] < item.value + opt[w]):
                opt[new_weight] = item.value + opt[w]
        weights.update(opt.keys())
    return max(opt.values())


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
