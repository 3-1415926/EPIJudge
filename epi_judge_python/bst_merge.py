from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


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

def bst_from_sorted_doubly_list(l: BstNode) -> Optional[BstNode]:
    if l is None: return None
    fast = slow = l
    while fast and fast.right:
        fast = fast.right.right
        slow = slow.right
    left_tail, right_head = slow.left, slow.right
    if left_tail: left_tail.right = slow.left = None
    if right_head: right_head.left = slow.right = None
    slow.left = bst_from_sorted_doubly_list(l if l is not slow else None)
    slow.right = bst_from_sorted_doubly_list(right_head)
    return slow

def merge_two_bsts(A: BstNode, B: BstNode) -> Optional[BstNode]:
    A = bst_to_doubly_linked_list(A)
    B = bst_to_doubly_linked_list(B)
    dummy_head = tail = BstNode()
    a_it, b_it = A, B
    while a_it and b_it:
        if a_it.data <= b_it.data: tail.right, a_it.left, a_it = a_it, tail, a_it.right
        else:                      tail.right, b_it.left, b_it = b_it, tail, b_it.right
        tail = tail.right
    if a_it: tail.right, a_it.left = a_it, tail
    if b_it: tail.right, b_it.left = b_it, tail
    if dummy_head.right: dummy_head.right.left = None
    return bst_from_sorted_doubly_list(dummy_head.right)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_merge.py', 'bst_merge.tsv',
                                       merge_two_bsts))
