from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    assert len(preorder) == len(inorder)
    if len(preorder) == 0: return None
    inorder_root_idx = inorder.index(preorder[0])
    return BinaryTreeNode(
        data=preorder[0],
        left=binary_tree_from_preorder_inorder(preorder[1:inorder_root_idx + 1], inorder[:inorder_root_idx]),
        right=binary_tree_from_preorder_inorder(preorder[inorder_root_idx + 1:], inorder[inorder_root_idx + 1:]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
