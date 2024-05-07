from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if L is None:
        return True
    fast = slow = L
    rev = None
    while fast is not None and fast.next is not None:
        temp = slow
        slow = slow.next
        fast = fast.next.next
        temp.next = rev
        rev = temp
    if fast is not None:
        slow = slow.next
    while rev is not None and slow is not None:
        if rev.data != slow.data:
            return False
        rev = rev.next
        slow = slow.next
    assert rev is None and slow is None
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
