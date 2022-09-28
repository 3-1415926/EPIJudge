from typing import Any
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def get_max(tree: BinaryTreeNode) -> Any:
    while tree.right:
        tree = tree.right
    return tree.data

def get_min(tree: BinaryTreeNode) -> Any:
    while tree.left:
        tree = tree.left
    return tree.data

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if tree is None: return True
    if tree.left and get_max(tree.left) > tree.data: return False
    if tree.right and get_min(tree.right) < tree.data: return False
    return is_binary_tree_bst(tree.left) and is_binary_tree_bst(tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
