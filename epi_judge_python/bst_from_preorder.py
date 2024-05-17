from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int],
                              start: int = 0, end: Optional[int] = None) -> Optional[BstNode]:
    if end is None:
        end = len(preorder_sequence)
    if start >= end:
        return None
    mid = start + 1
    while mid < end and preorder_sequence[mid] < preorder_sequence[start]:
        mid += 1        
    return BstNode(preorder_sequence[start],
                   rebuild_bst_from_preorder(preorder_sequence, start + 1, mid),
                   rebuild_bst_from_preorder(preorder_sequence, mid, end))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
