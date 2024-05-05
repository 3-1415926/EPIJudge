from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start == finish:
        return L
    if start > finish:
        start, finish = finish, start
    dummy_head = ListNode(next=L)
    ptr = dummy_head
    before, after = None, None
    for i in range(finish):
        if i == start - 1:
            before = ptr
        ptr = ptr.next
        if i == finish - 1:
            after = ptr.next
    tail = after
    ptr = before.next
    while ptr != after:
        next = ptr.next
        ptr.next = tail
        tail = ptr
        ptr = next
    before.next = tail
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))


