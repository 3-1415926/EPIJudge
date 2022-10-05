import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def bst_to_doubly_linked_list(tree: BstNode) -> Optional[BstNode]:
    if tree is None: return None
    left_head = bst_to_doubly_linked_list(tree.left)
    left_tail = left_head
    while left_tail and left_tail.right: left_tail = left_tail.right
    right_head = bst_to_doubly_linked_list(tree.right)
    tree.right = right_head
    if right_head: right_head.left = tree
    tree.left = left_tail
    if left_tail: left_tail.right = tree
    return left_head or tree
    

@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_to_sorted_list.py',
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
