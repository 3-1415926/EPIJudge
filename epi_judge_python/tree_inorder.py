from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack = []
    result = []
    while True:
        if tree:
            stack.append(tree)
            tree = tree.left
        elif stack:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right
        else:
            break
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
