from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even_dummy_head = even_tail = ListNode()
    odd_dummy_head = odd_tail = ListNode()
    i = 0
    while L is not None:
        next = L.next
        L.next = None
        if i % 2 == 0:
            even_tail.next = L
            even_tail = even_tail.next
        else:
            odd_tail.next = L
            odd_tail = odd_tail.next
        L = next
        i += 1
    even_tail.next = odd_dummy_head.next      
    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
