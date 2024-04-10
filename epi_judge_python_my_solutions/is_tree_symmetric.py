from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def check_symmetric(a: BinaryTreeNode, b: BinaryTreeNode) -> bool:
    if a is None:
        if b is None: return True
        else: return False
    else:
        if b is None: return False
        else: return a.data == b.data and check_symmetric(a.left, b.right) and check_symmetric(a.right, b.left)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree is None: return True
    return check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
