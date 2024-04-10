from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L
    fast, slow = L.next, L
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    half = slow.next
    slow.next = None
    del fast, slow
    L = stable_sort_list(L)
    half = stable_sort_list(half)
    dummy_head = dummy_tail = ListNode()
    while L is not None and half is not None:
        if L.data <= half.data:
            dummy_tail.next = L
            L = L.next
        else:
            dummy_tail.next = half
            half = half.next
        dummy_tail = dummy_tail.next
        dummy_tail.next = None
    dummy_tail.next = L or half
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
