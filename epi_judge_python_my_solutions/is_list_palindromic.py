from multiprocessing import dummy
from list_node import ListNode
from test_framework import generic_test


# L,t                       L    t                   L         t
# [1]-> 2 -> 3 -> None  |  [2 -> 1]-> 3 -> None  |  [3 -> 2 -> 1]-> None
def reverse_list(L: ListNode) -> ListNode:
    if L is None: return None
    tail = L
    while tail.next is not None:
        previous = L
        L = tail.next
        tail.next = L.next
        L.next = previous
    return L


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if L is None: return True
    fast = slow = L
    while fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    slow = reverse_list(slow)
    it1, it2 = L, slow
    while it1 is not None and it2 is not None and it1.data == it2.data:
        it1, it2 = it1.next, it2.next
    result = it2 is None
    slow = reverse_list(slow)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
