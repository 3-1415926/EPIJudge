from collections import deque
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


NEXT_LEVEL = object()

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []
    result = []
    queue = deque([NEXT_LEVEL, tree])
    while queue:
        node = queue.popleft()
        if node is NEXT_LEVEL:
            if queue:
                queue.append(NEXT_LEVEL)
            result.append([])
            continue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        result[-1].append(node.data)
    if not result[-1]:
        result.pop()
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
