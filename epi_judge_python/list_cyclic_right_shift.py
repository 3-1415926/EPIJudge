from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if L is None: return None
    slow = fast = dummy_head = ListNode(next=L)
    while True:
        for i in range(k):
            fast = fast.next
            if fast.next is None:
                fast = dummy_head
                k %= (i + 1)
                break
        else:
            break
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    fast.next = L
    L = slow.next
    slow.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
