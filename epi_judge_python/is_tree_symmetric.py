from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def are_mirrored(left: BinaryTreeNode, right: BinaryTreeNode) -> bool:
    if not left and not right:
        return True
    if (not left) ^ (not right):
        return False
    return left.data == right.data and are_mirrored(left.left, right.right) and are_mirrored(left.right, right.left)
        

def is_symmetric(tree: BinaryTreeNode) -> bool:
    return True if not tree else are_mirrored(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
