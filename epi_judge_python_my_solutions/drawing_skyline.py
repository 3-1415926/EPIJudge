import collections
import functools
from multiprocessing.sharedctypes import Value
import traceback
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class Rect(collections.namedtuple('Rect', ('left', 'right', 'height'))):
    def __repr__(self):
        return f'[{self.left},{self.right}]^{self.height}'

    def maybe_raise_height(self, height: int) -> 'Rect':
        return self if self.height >= height else Rect(self.left, self.right, height)

def ceil_pow2(number):
    result = 1
    while result < number:
        result <<= 1
    return result

# -0%1 -1%2   -3%3   -3%4      -7%5        -7%6         -7%7         -7%8
#   0    0      0      0         0           0            0            0
#   j   1 2    1 2    1 2      1   2      1     2      1     2      1     2
#       j k   34 l   34 56    3 4 5 6    3 4   5 6    3 4   5 6    3 4   5 6
#             jk     jk lm   78 l m n   78 9A  n o   78 9A BC p   78 9A BC DE
class MaxTree:             # jk         jk lm        jk lm no     jk lm no pq
    def __init__(self, slots):
        self._slots = slots
        self._tree = [None] * (len(self._slots) * 2 - 1)
        self._leaf_base = ceil_pow2(len(self._slots)) - 1
        for i in reversed(range(len(self._tree))):
            if i * 2 + 1 >= len(self._tree):
                slot_idx = (i - self._leaf_base) % len(self._slots)
                self._tree[i] = Rect(self._slots[slot_idx], self._slots[slot_idx], 0)
            else:
                child_idx = i * 2 + 1
                self._tree[i] = Rect(self._tree[child_idx].left, self._tree[child_idx + 1].right, 0)

    def raise_max(self, left: int, right: int, height: int, *, idx: int = 0):
        if idx >= len(self._tree): raise ValueError()
        left = max(left, self._tree[idx].left)
        right = min(right, self._tree[idx].right)
        if left > right: return
        if left == self._tree[idx].left and self._tree[idx].right == right:
            self._tree[idx] = self._tree[idx].maybe_raise_height(height)
        else:
            self.raise_max(left, right, height, idx=idx * 2 + 1)
            self.raise_max(left, right, height, idx=idx * 2 + 2)

    def get_max(self, left: int, right: int, *, idx: int = 0) -> int:
        if idx >= len(self._tree): raise ValueError()
        left = max(left, self._tree[idx].left)
        right = min(right, self._tree[idx].right)
        if left > right: return 0
        result = self._tree[idx].height
        if idx * 2 + 1 < len(self._tree):
            result = max(result, self.get_max(left, right, idx=idx * 2 + 1))
            result = max(result, self.get_max(left, right, idx=idx * 2 + 2))
        return result

    def __repr__(self):
        return str(self._tree)

def compute_skyline(buildings: List[Rect]) -> List[Rect]:
    if len(buildings) == 0: return buildings
    slots = {bo for bu in buildings for bo in (bu.left - 1, bu.left, bu.right, bu.right + 1)}
    slots.remove(min(slots))
    slots.remove(max(slots))
    slots = sorted(slots)
    max_tree = MaxTree(slots)
    for building in buildings:
        max_tree.raise_max(*building)
    results = []
    for i in range(len(slots)):
        height = max_tree.get_max(slots[i], slots[i])
        if not results or results[-1].height != height:
            results.append(Rect(slots[i], slots[i], height))
        else:
            results[-1] = Rect(results[-1].left, slots[i], height)
    return results


@enable_executor_hook
def compute_skyline_wrapper(executor, buildings):
    buildings = [Rect(*x) for x in buildings]

    result = executor.run(functools.partial(compute_skyline, buildings))

    return [(x.left, x.right, x.height) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('drawing_skyline.py',
                                       'drawing_skyline.tsv',
                                       compute_skyline_wrapper))
