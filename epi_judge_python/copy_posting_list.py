import functools
from typing import Optional

from posting_list_node import PostingListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def copy_postings_list(L: PostingListNode) -> Optional[PostingListNode]:
    if not L:
        return L
    orig = L
    while orig:
        copy = PostingListNode(order=orig.order, next=orig.next)
        orig.next = copy
        orig = copy.next
    orig = L
    while orig:
        copy = orig.next
        copy.jump = orig.jump.next if orig.jump else None
        orig = orig.next.next
    copy_head = L.next
    orig = L
    while orig:
        copy = orig.next
        assert copy
        orig.next, copy.next = orig.next.next, copy.next.next if copy.next else None
        orig = orig.next
    return copy_head


def assert_lists_equal(orig, copy):
    node_mapping = dict()
    o_it = orig
    c_it = copy
    while o_it:
        if not c_it:
            raise TestFailure('Copied list has fewer nodes than the original')
        if o_it.order != c_it.order:
            raise TestFailure('Order value mismatch')
        node_mapping[o_it] = c_it
        o_it = o_it.next
        c_it = c_it.next

    if c_it:
        raise TestFailure('Copied list has more nodes than the original')

    o_it = orig
    c_it = copy
    while o_it:
        if c_it in node_mapping:
            raise TestFailure(
                'Copied list contains a node from the original list')
        if o_it.jump is None:
            if c_it.jump is not None:
                raise TestFailure(
                    'Jump link points to a different nodes in the copied list')
        else:
            if not node_mapping[o_it.jump] is c_it.jump:
                raise TestFailure(
                    'Jump link points to a different nodes in the copied list')
        o_it = o_it.next
        c_it = c_it.next


@enable_executor_hook
def copy_postings_list_wrapper(executor, l):
    def create_posting_list(serialized):
        key_mapping = dict()
        head = None
        for (order, _) in reversed(serialized):
            head = PostingListNode(order, head)
            key_mapping[order] = head

        list_it = head
        for (_, jump_index) in serialized:
            if jump_index != -1:
                list_it.jump = key_mapping.get(jump_index, None)
                if not list_it.jump:
                    raise RuntimeError('Jump index out of range')

        return head

    head = create_posting_list(l)

    copy = executor.run(functools.partial(copy_postings_list, head))

    assert_lists_equal(head, copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('copy_posting_list.py',
                                       'copy_posting_list.tsv',
                                       copy_postings_list_wrapper))
