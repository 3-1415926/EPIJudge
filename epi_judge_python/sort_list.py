from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def append(tail: ListNode, L: ListNode):
    tail.next = L
    tail = tail.next
    L = L.next
    tail.next = None
    return tail, L    


def concatenate(*Ls: ListNode) -> Optional[ListNode]:
    head = tail = ListNode()
    for L in Ls:
        while L:
            tail, L = append(tail, L)
    return head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if not L: return L
    pivot = L.data
    lt_head = lt_tail = ListNode()
    eq_head = eq_tail = ListNode()
    gt_head = gt_tail = ListNode()
    while L:
        if L.data < pivot:
            lt_tail, L = append(lt_tail, L)
        elif L.data > pivot:
            gt_tail, L = append(gt_tail, L)
        else:
            eq_tail, L = append(eq_tail, L)
    del lt_tail, eq_tail, gt_tail
    lt_head.next = stable_sort_list(lt_head.next)
    gt_head.next = stable_sort_list(gt_head.next)
    return concatenate(lt_head.next, eq_head.next, gt_head.next)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
