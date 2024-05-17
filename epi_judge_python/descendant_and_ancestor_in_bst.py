import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    a, b = possible_anc_or_desc_0, possible_anc_or_desc_1
    if not a or not b or not middle:
        return False
    while a and a.data != middle.data or b and b.data != middle.data:
        if a:
            if middle.data < a.data:
                a = a.left
            elif middle.data > a.data:
                a = a.right
        if b:
            if middle.data < b.data:
                b = b.left
            elif middle.data > b.data:
                b = b.right
    if not (bool(a) ^ bool(b)):
        return False
    descendant = possible_anc_or_desc_1 if a else possible_anc_or_desc_0
    while middle and middle.data != descendant.data:
        if descendant.data < middle.data:
            middle = middle.left
        elif descendant.data > middle.data:
            middle = middle.right
    return bool(middle)


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
