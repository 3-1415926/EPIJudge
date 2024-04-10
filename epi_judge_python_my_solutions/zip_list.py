from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_list(L: ListNode) -> Optional[ListNode]:
    if L is None: return None
    prev, cur = None, L
    while cur:
        temp = cur.next
        cur.next, prev, cur = prev, cur, temp
    return prev


def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
    if L is None: return None
    fast, slow = L.next, L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    fast = reverse_list(slow.next)
    slow.next = None
    slow = L
    while fast:
        slow_next, fast_next = slow.next, fast.next
        slow.next, fast.next = fast, slow_next
        slow, fast = slow_next, fast_next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                       zipping_linked_list))
