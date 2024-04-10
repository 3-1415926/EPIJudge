from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    result_head = result_tail = ListNode(data=0)
    carry = 0
    while True:
        result_tail.data = (L1.data if L1 is not None else 0) + (L2.data if L2 is not None else 0) + carry
        carry, result_tail.data = result_tail.data // 10, result_tail.data % 10
        if L1 is not None: L1 = L1.next
        if L2 is not None: L2 = L2.next
        if L1 is None and L2 is None and carry == 0: break
        result_tail.next = result_tail = ListNode(data=0)
    return result_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
