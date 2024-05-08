import functools
from typing import Iterable, List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def leaves_and_boundaries(tree: BinaryTreeNode,
                          left_boundary: bool = False,
                          right_boundary: bool = False) -> Iterable[BinaryTreeNode]:
    if not tree:
        return
    if not tree.left and not tree.right:
        yield tree
    else:
        if left_boundary:
            yield tree
        for node in leaves_and_boundaries(tree.left,
                                          left_boundary=left_boundary,
                                          right_boundary=right_boundary and not tree.right):
            yield node
        for node in leaves_and_boundaries(tree.right,
                                          left_boundary=left_boundary and not tree.left,
                                          right_boundary=right_boundary):
            yield node
        if right_boundary:
            yield tree

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree: return []
    return [tree,
            *leaves_and_boundaries(tree.left, left_boundary=True),
            *leaves_and_boundaries(tree.right, right_boundary=True)]


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
