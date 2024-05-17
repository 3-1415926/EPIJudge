import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    if not tree:
        return []
    if tree.data <= interval.left:
        return ([] if tree.data != interval.left else [tree.data]) + range_lookup_in_bst(tree.right, interval)
    if tree.data >= interval.right:
        return range_lookup_in_bst(tree.left, interval) + ([] if tree.data != interval.right else [tree.data])
    return range_lookup_in_bst(tree.left, interval) + [tree.data] + range_lookup_in_bst(tree.right, interval)


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
