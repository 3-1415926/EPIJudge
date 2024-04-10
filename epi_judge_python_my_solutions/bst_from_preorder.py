import bisect
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int], left: int = 0, right: int = None) -> Optional[BstNode]:
    if right is None: right = len(preorder_sequence)
    if right <= left: return None
    root = BstNode(data=preorder_sequence[left])
    mid = bisect.bisect_left(preorder_sequence, preorder_sequence[left], left + 1, right)
    root.left = rebuild_bst_from_preorder(preorder_sequence, left + 1, mid)
    root.right = rebuild_bst_from_preorder(preorder_sequence, mid, right)
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
