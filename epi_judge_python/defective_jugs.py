import collections
import functools
import heapq
import itertools
import traceback
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class Jug(collections.namedtuple('Jug', ('low', 'high'))):
    def contains(self, other):
        return self.low <= other.low and other.high <= self.high

    @property
    def spread(self):
        return self.high - self.low

    def __add__(self, other):
        return Jug(self.low + other.low, self.high + other.high)

    def __repr__(self):
        return f'{self.low}..{self.high}'


def purge(jugs: List[Jug]):
    if not jugs: return
    i = 0
    for j in range(1, len(jugs)):
        if jugs[i].low != jugs[j].low:
            i += 1
            jugs[i] = jugs[j]
        elif jugs[i].high > jugs[j].high:
            jugs[i] = jugs[j]
    del jugs[i+1:]

def check_feasible(jugs: List[Jug], L: int, H: int) -> bool:
    jugs.sort()
    purge(jugs)
    target = Jug(L, H)
    feasible = [Jug(0, 0)]
    for jug in reversed(jugs):
        newly_feasible = []
        for fea in feasible:
            newly_feasible.append([])
            while True:
                fea += jug
                if fea.high > target.high: break
                if fea.spread > target.spread: break
                if target.contains(fea): return True
                newly_feasible[-1].append(fea)
        newly_feasible.append(feasible)
        feasible = list(heapq.merge(*newly_feasible))
        purge(feasible)
    return False


@enable_executor_hook
def check_feasible_wrapper(executor, jugs, l, h):
    jugs = [Jug(*x) for x in jugs]
    return executor.run(functools.partial(check_feasible, jugs, l, h))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('defective_jugs.py',
                                       'defective_jugs.tsv',
                                       check_feasible_wrapper))
