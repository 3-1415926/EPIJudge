from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
    slow_head = None
    slow = fast = L
    while fast:
        fast = fast.next
        slow.next, slow_head, slow = slow_head, slow, slow.next
        if fast:
            fast = fast.next
        else:
            break
    else:
        slow_head, slow = slow, slow_head
    result = None
    while slow_head:
        slow_head.next, result, slow_head = result, slow_head, slow_head.next
        if slow:
            slow.next, result, slow = result, slow, slow.next
        else:
            break
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                       zipping_linked_list))
