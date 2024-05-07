import functools
from typing import Union

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Union[BinaryTreeNode, int]:
    if tree is None:
        return 0
    res_left = lca(tree.left, node0, node1)
    if not isinstance(res_left, int):
        return res_left
    res_right = lca(tree.right, node0, node1)
    if not isinstance(res_right, int):
        return res_right
    num_found = res_left + res_right + int(tree is node0) + int(tree is node1)
    assert 0 <= num_found <= 2
    return num_found if num_found <= 1 else tree


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
