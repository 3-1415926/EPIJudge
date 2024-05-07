from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode, prefix: int = 0) -> int:
    if not tree:
        return 0
    prefix = (prefix << 1) | tree.data
    if not tree.left and not tree.right:
        return prefix
    result = 0
    if tree.left:
        result += sum_root_to_leaf(tree.left, prefix)
    if tree.right:
        result += sum_root_to_leaf(tree.right, prefix)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
