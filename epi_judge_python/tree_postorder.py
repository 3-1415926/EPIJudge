from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if tree is None: return []
    result, stack = [], [tree]
    while stack:
        tree = stack.pop()
        result.append(tree.data)
        if tree.left: stack.append(tree.left)
        if tree.right: stack.append(tree.right)
    result.reverse()
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
