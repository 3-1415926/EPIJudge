from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    if not tree:
        return []
    right_result = find_k_largest_in_bst(tree.right, k)
    if len(right_result) >= k:
        return right_result
    elif len(right_result) == k - 1:
        return [tree.data] + right_result
    else:
        return find_k_largest_in_bst(tree.left, k - len(right_result) - 1) + [tree.data] + right_result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
