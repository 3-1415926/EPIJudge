from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    if L is None: return None
    ptr = L
    while ptr.next is not None:
        if ptr.data == ptr.next.data:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
