from multiprocessing import dummy
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if L is None: return None
    tail = L
    length = 1
    while tail.next != None:
        tail = tail.next
        length += 1
    tail.next = L
    for _ in range(-k % length):
        tail = tail.next
    L = tail.next
    tail.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
