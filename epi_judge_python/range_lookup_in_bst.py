import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval, result: List[int] = None) -> List[int]:
    if result is None: result = []
    if tree is not None and interval.left <= interval.right:
        range_lookup_in_bst(tree.left, Interval(interval.left, min(tree.data - 1, interval.right)), result)
        if interval.left <= tree.data <= interval.right:
            result.append(tree.data)
        range_lookup_in_bst(tree.right, Interval(max(tree.data + 1, interval.left), interval.right), result)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
