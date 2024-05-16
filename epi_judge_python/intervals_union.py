import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
TypedEndpoint = collections.namedtuple('TypedEndpoint', ('endpoint', 'is_right'))
Interval = collections.namedtuple('Interval', ('left', 'right'))

def get_endpoint_key(e):
    # LC -> RO -> LO -> RC = -2, -1, 1, 2
    return e.endpoint.val, (-(e.is_right ^ e.endpoint.is_closed) * 2 + 1) * (e.endpoint.is_closed + 1)


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    endpoints = [e for i in intervals for e in (TypedEndpoint(i.left, False), TypedEndpoint(i.right, True))]
    endpoints.sort(key=get_endpoint_key)
    in_flight = 0
    result = []
    start = None
    for e in endpoints:
        if not e.is_right:
            if in_flight == 0:
                assert start is None
                start = e
            in_flight += 1
        else:
            in_flight -= 1
            if in_flight == 0:
                result.append(Interval(start.endpoint, e.endpoint))
                start = None
    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
