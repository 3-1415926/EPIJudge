import functools
from typing import Optional, Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def find_lca(tree: Optional[BinaryTreeNode], node1: BinaryTreeNode, node2: BinaryTreeNode) -> Tuple[Optional[BinaryTreeNode], bool, bool]:
    if tree is None: return None, False, False
    left_lca, left_found1, left_found2 = find_lca(tree.left, node1, node2)
    if left_lca:
        assert left_found1 and left_found2
        return left_lca, True, True
    right_lca, right_found1, right_found2 = find_lca(tree.right, node1, node2)
    if right_lca:
        assert right_found1 and right_found2
        return right_lca, True, True
    found1 = tree is node1 or left_found1 or right_found1
    found2 = tree is node2 or left_found2 or right_found2
    return tree if found1 and found2 else None, found1, found2



def lca(tree: BinaryTreeNode, node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    result, _, _ = find_lca(tree, node1, node2)
    return result


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
