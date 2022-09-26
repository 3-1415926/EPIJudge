import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def is_leaf(tree):
    return tree.left is None and tree.right is None

def leaves(tree):
    if tree is None: return []
    if is_leaf(tree): return [tree]
    return leaves(tree.left) + leaves(tree.right)

def left_boundary(tree):
    if tree is None or is_leaf(tree): return []
    return [tree] + (left_boundary(tree.left) if tree.left else left_boundary(tree.right))

def right_boundary(tree):
    if tree is None or is_leaf(tree): return []
    return (right_boundary(tree.right) if tree.right else right_boundary(tree.left)) + [tree]

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if tree is None: return []
    return [tree] + left_boundary(tree.left) + leaves(tree.left) + leaves(tree.right) + right_boundary(tree.right)



def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
