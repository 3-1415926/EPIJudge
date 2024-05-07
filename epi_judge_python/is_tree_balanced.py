from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return True if not tree else (
        is_balanced_binary_tree(tree.left) and
        is_balanced_binary_tree(tree.right) and
        abs(get_height(tree.left) - get_height(tree.right)) <= 1)


def get_height(tree: BinaryTreeNode) -> int:
    return 0 if not tree else 1 + max(get_height(tree.left), get_height(tree.right))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
