from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode()
    dummy_tail = dummy_head
    while L1 and L2:
        if L1.data <= L2.data:
            dummy_tail.next = L1
            dummy_tail = L1
            L1 = L1.next
        else:
            dummy_tail.next = L2
            dummy_tail = L2
            L2 = L2.next
    if L1:
        dummy_tail.next = L1
    elif L2:
        dummy_tail.next = L2
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
