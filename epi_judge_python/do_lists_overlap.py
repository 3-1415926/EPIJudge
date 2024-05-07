import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_cycle(l: ListNode) -> Optional[ListNode]:
    fast = slow = l
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return fast
    return None


def get_length(l: ListNode) -> int:
    length = 0
    while l is not None:
        length += 1
        l = l.next
    return length


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    c0 = get_cycle(l0)
    c1 = get_cycle(l1)
    if c0 is None and c1 is None:
        len0 = get_length(l0)
        len1 = get_length(l1)
        min_len = min(len0, len1)
        for _ in range(len0 - min_len):
            l0 = l0.next
        for _ in range(len1 - min_len):
            l1 = l1.next
        while l0 is not None and l1 is not None and l0 != l1:
            l0 = l0.next
            l1 = l1.next
        return l0 if l0 is l1 else None
    elif c0 is not None and c1 is not None:
        ptr = c0.next
        while ptr is not c0 and ptr is not c1:
            ptr = ptr.next
        return ptr if ptr is c1 else None
    else:
        return None


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
