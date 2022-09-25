import functools
from typing import Optional, Tuple

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(lst: ListNode) -> Tuple[Optional[ListNode], Optional[int]]:
    fast = slow = lst
    while fast is not None and fast.next is not None and slow is not None:
        fast, slow = fast.next.next, slow.next
        if fast is slow: break
    else:
        return None, None
    length = 0
    while True:
        fast = fast.next
        length += 1
        if fast is slow: break
    fast = slow = lst
    for _ in range(length):
        fast = fast.next
    while fast is not slow:
        fast, slow = fast.next, slow.next
    return fast, length


def get_distance(from_: ListNode, to: Optional[ListNode] = None) -> int:
    length = 0
    while from_ is not to:
        from_ = from_.next
        length += 1
    return length


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    len0 = get_distance(l0)
    len1 = get_distance(l1)
    if len0 < len1:
        len0, len1 = len1, len0
        l0, l1 = l1, l0
    while len0 > len1:
        l0 = l0.next
        len0 -= 1
    while l0 is not l1:
        l0, l1 = l0.next, l1.next
    return l0


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    c0, clen0 = has_cycle(l0)
    c1, clen1 = has_cycle(l1)
    if clen0 != clen1:
        return None
    if c0 is None:
        assert c1 is None
        return overlapping_no_cycle_lists(l0, l1)
    assert c1 is not None and clen0 == clen1
    temp = c0
    while True:
        temp = temp.next
        if temp is c0 or temp is c1: break
    if temp is not c1:
        return None
    slen0 = get_distance(l0, c0)
    slen1 = get_distance(l1, c1)
    if slen0 < slen1:
        slen0, slen1 = slen1, slen0
        c0, c1 = c1, c0
        l0, l1 = l1, l0
    while slen0 > slen1:
        l0 = l0.next
        slen0 -= 1
    while l0 is not l1 and l0 is not c0 and l1 is not c1:
        l0, l1 = l0.next, l1.next
    return l0 if l0 is l1 else c0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
