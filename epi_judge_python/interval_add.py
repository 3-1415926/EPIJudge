import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def do_intersect(a: Interval, b: Interval):
    if a.left > b.left: a, b = b, a
    return a.left <= b.left <= a.right or a.left <= b.right <= a.right

def union(a: Interval, b: Interval):
    return Interval(min(a.left, b.left), max(a.right, b.right))


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    result = [new_interval]
    for interval in disjoint_intervals:
        if not do_intersect(interval, result[0]):
            result.append(interval)
        else:
            result[0] = union(result[0], interval)
    result.sort()
    return result


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
