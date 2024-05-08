from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int],
                                      pre_left: int = 0, pre_right: Optional[int] = None,
                                      in_left: int = 0, in_right: Optional[int] = None) -> BinaryTreeNode:
    if pre_right is None: pre_right = len(preorder)
    if in_right is None: in_right = len(inorder)
    assert pre_right - pre_left == in_right - in_left
    if pre_right - pre_left == 0:
        return None
    root_in_idx = None
    for in_idx in range(in_left, in_right):
        if inorder[in_idx] == preorder[pre_left]:
            root_in_idx = in_idx
            break
    len_left = root_in_idx - in_left
    len_right = in_right - root_in_idx - 1
    left = binary_tree_from_preorder_inorder(preorder, inorder, pre_left + 1, pre_left + 1 + len_left, in_left, root_in_idx)
    right = binary_tree_from_preorder_inorder(preorder, inorder, pre_left + 1 + len_left, pre_right, root_in_idx + 1, in_right)
    return BinaryTreeNode(data=preorder[pre_left], left=left, right=right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
