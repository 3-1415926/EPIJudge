import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    if not preorder:
        return None
    stack = []
    for datum in reversed(preorder):
        if datum is None:
            stack.append(datum)
        else:
            left = stack.pop()
            right = stack.pop()
            stack.append(BinaryTreeNode(data=datum, left=left, right=right))
    assert len(stack) == 1
    return stack[0]


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
