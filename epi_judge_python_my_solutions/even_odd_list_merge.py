from inspect import trace
from typing import Optional
import traceback

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None: return L
    even_head = even_tail = L
    odd_head = odd_tail = L.next
    while even_tail.next is not None:
        even_tail.next = even_tail.next.next
        if even_tail.next is not None:
            even_tail = even_tail.next
        if odd_tail.next is not None:
            odd_tail.next = odd_tail.next.next
        if odd_tail.next is not None:
            odd_tail = odd_tail.next
    assert even_tail.next is None and odd_tail.next is None
    even_tail.next = odd_head
    return even_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
