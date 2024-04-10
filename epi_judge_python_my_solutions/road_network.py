import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

HighwaySection = collections.namedtuple('HighwaySection',
                                        ('x', 'y', 'distance'))


def find_best_proposals(H: List[HighwaySection], P: List[HighwaySection],
                        n: int) -> HighwaySection:
    A = [[float('inf') if j != i else 0 for j in range(n)] for i in range(n)]
    for h in H:
        A[h.x][h.y] = A[h.y][h.x] = h.distance
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][j] > A[i][k] + A[k][j]:
                    A[i][j] = A[i][k] + A[k][j]
    best_delta, best_p = float('inf'), None
    for p in P:
        delta = 0
        for i in range(n):
            for j in range(n):
                delta += min((0,
                                    A[i][p.x] + p.distance + A[p.y][j] - A[i][j],
                                    A[i][p.y] + p.distance + A[p.x][j] - A[i][j]))
        if delta < best_delta:
            best_delta = delta
            best_p = p
    return best_p


@enable_executor_hook
def find_best_proposals_wrapper(executor, H, P, n):
    H = [HighwaySection(*x) for x in H]
    P = [HighwaySection(*x) for x in P]

    return executor.run(functools.partial(find_best_proposals, H, P, n))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('road_network.py',
                                       'road_network.tsv',
                                       find_best_proposals_wrapper,
                                       res_printer=res_printer))
