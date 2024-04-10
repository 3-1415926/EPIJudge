import functools
from typing import List, Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_recursive(preorder: List[int], index: int) -> Tuple[BinaryTreeNode, int]:
    if preorder[index] is None: return None, index + 1
    root = BinaryTreeNode(data=preorder[index])
    index += 1
    root.left, index = reconstruct_recursive(preorder, index)
    root.right, index = reconstruct_recursive(preorder, index)
    return root, index



def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    root, index = reconstruct_recursive(preorder, 0)
    assert index == len(preorder)
    return root


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
