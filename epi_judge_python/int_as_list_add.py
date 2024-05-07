from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    if L1 is None: return L2
    if L2 is None: return L1
    dummy_head = tail = ListNode()
    carry = 0
    while L1 is not None or L2 is not None or carry != 0:
        if L1 is not None:
            carry += L1.data
            L1 = L1.next
        if L2 is not None:
            carry += L2.data
            L2 = L2.next
        tail.next = ListNode(data=carry % 10)
        tail = tail.next
        carry //= 10
    return ListNode(data=0) if dummy_head.next is None else dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
