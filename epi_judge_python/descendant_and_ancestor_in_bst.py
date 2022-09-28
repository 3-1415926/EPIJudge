import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def descend_step(tree: BstNode, target: BstNode) -> BstNode:
    if tree is None: return None
    assert target.data != tree.data
    if target.data < tree.data: return tree.left
    else: return tree.right

def matches_nodes(node: BstNode, *candidates: BstNode) -> bool:
    if node is None: return False
    return node.data in (c.data for c in candidates)


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    if matches_nodes(middle, possible_anc_or_desc_0, possible_anc_or_desc_1): return False
    if matches_nodes(possible_anc_or_desc_0, possible_anc_or_desc_1): return False
    it0, it1 = possible_anc_or_desc_0, possible_anc_or_desc_1
    while (it0 or it1) and not matches_nodes(it0, middle, possible_anc_or_desc_1) and not matches_nodes(it1, middle, possible_anc_or_desc_0):
        it0 = descend_step(it0, middle)
        it1 = descend_step(it1, middle)
    if matches_nodes(it1, middle):
        it0, it1 = it1, it0
        possible_anc_or_desc_0, possible_anc_or_desc_1 = possible_anc_or_desc_1, possible_anc_or_desc_0
    if matches_nodes(it0, middle):
        while it0 and not matches_nodes(it0, possible_anc_or_desc_1):
            it0 = descend_step(it0, possible_anc_or_desc_1)
        return matches_nodes(it0, possible_anc_or_desc_1)
    return False



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
