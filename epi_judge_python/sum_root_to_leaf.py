from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode, path: int = 0) -> int:
    if tree is None: return 0
    path += tree.data
    if tree.left is None and tree.right is None: return path
    return (sum_root_to_leaf(tree.left, path << 1) if tree.left else 0) + (
            sum_root_to_leaf(tree.right, path << 1) if tree.right else 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
