import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_length(l: ListNode) -> int:
    length = 0
    while l is not None:
        length += 1
        l = l.next
    return length


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    l0_len = get_length(l0)
    l1_len = get_length(l1)
    min_len = min(l0_len, l1_len)
    for _ in range(l0_len - min_len):
        l0 = l0.next
    for _ in range(l1_len - min_len):
        l1 = l1.next
    while l0 is not None and l1 is not None:
        if l0 is l1:
            return l0
        l0 = l0.next
        l1 = l1.next
    assert l0 is None and l1 is None
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
