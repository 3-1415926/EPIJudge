from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if tree is None: return False
    remaining_weight -= tree.data
    if tree.left is None and tree.right is None: return remaining_weight == 0
    return has_path_sum(tree.left, remaining_weight) or has_path_sum(tree.right, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
