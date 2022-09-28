import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

# \ closed               Sort order:     
# right \  F  T         
#   F     +1 -2         -2 -1 +1 +2
#   T     -1 +2          [  )  (  ]
class SortableEndpoint(collections.namedtuple('SortableEndpoint', ('val', 'kind_side'))):
    @staticmethod
    def make(val, is_right, is_closed):
        return SortableEndpoint(val, (2 if is_closed else 1) * (-1 if is_right ^ is_closed else 1))

    @property
    def is_closed(self):
        return abs(self.kind_side) == 2

    @property
    def is_right(self):
        return self.is_closed ^ (self.kind_side < 0)

    def __repr__(self):
        return (('[' if     self.is_closed and not self.is_right else
                 '(' if not self.is_closed and not self.is_right else '') + 
                 str(self.val) +
                (')' if not self.is_closed and self.is_right else
                 ']' if     self.is_closed and self.is_right else ''))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    endpoints = []
    for i in intervals:
        endpoints.append(SortableEndpoint.make(i.left.val, False, i.left.is_closed))
        endpoints.append(SortableEndpoint.make(i.right.val, True, i.right.is_closed))
    endpoints.sort()
    results = []
    overlap = 0
    start = None
    for e in endpoints:
        if not e.is_right:
            if overlap == 0: start = e
            overlap += 1
        else:
            overlap -= 1
            if overlap == 0: results.append(Interval(Endpoint(start.is_closed, start.val),
                                                     Endpoint(e.is_closed, e.val)))
    return results


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
