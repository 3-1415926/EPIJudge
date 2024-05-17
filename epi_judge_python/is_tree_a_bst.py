from typing import Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_bst_with_range(tree: BinaryTreeNode) -> Tuple[bool, int, int]:
    if not tree:
        return True, None, None
    left_bst, left_min, left_max = is_bst_with_range(tree.left)
    right_bst, right_min, right_max = is_bst_with_range(tree.right)
    return (left_bst and right_bst and (left_max <= tree.data if tree.left else True) and (tree.data <= right_min if tree.right else True),
            left_min if tree.left else tree.data,
            right_max if tree.right else tree.data) 

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_bst_with_range(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
