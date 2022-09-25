from typing import Optional

from list_node import ListNode
from test_framework import generic_test
 
#      pre   sl  pst                  |      pre        sl  pst     |      pre             sl  pst
# ph -> 1 ->[2]-> 3 -> 4 -> 5 -> None | ph -> 1 ->[3 -> 2]-> 4 -> 5 | ph -> 1 ->[4 -> 3 -> 2]-> 5
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if L is None or start == 0 or finish == 0: return L
    if start > finish: start, finish = finish, start
    pre_head = pre_sublist = ListNode(next=L)
    for _ in range(1, start):
        pre_sublist = pre_sublist.next
    sublist_last = pre_sublist.next
    for _ in range(finish - start):
        post_sublist = sublist_last.next
        post_sublist.next, sublist_last.next, pre_sublist.next = pre_sublist.next, post_sublist.next, post_sublist
        
    return pre_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
