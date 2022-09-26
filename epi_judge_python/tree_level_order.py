from typing import List

from collections import deque, namedtuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


NodeDepth = namedtuple('NodeDepth', 'node, depth')


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None: return []
    results = []
    queue = deque([NodeDepth(tree, 0)])
    while len(queue) > 0:
        node, depth = queue.popleft()
        if len(results) <= depth:
            results.append([])
        results[depth].append(node.data)
        if node.left: queue.append(NodeDepth(node.left, depth + 1))
        if node.right: queue.append(NodeDepth(node.right, depth + 1))
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
