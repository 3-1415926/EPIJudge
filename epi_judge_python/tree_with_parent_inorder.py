from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, result = None, []
    while tree:
        if prev == tree.parent:
            if tree.left:
                prev, tree = tree, tree.left
                continue
        if not tree.right or prev is not tree.right:
            result.append(tree.data)
        if tree.right and prev is not tree.right:
            prev, tree = tree, tree.right
            continue
        prev, tree = tree, tree.parent
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
