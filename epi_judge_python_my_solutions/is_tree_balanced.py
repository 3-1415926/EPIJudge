from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple


def check_balanced(root: BinaryTreeNode) -> Tuple[bool, int]:
    if root is None: return True, 0
    left_balanced, left_height = check_balanced(root.left)
    if not left_balanced: return False, None
    right_balanced, right_height = check_balanced(root.right)
    if not right_balanced: return False, None
    return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return check_balanced(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
