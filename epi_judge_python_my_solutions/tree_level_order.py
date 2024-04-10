from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test



def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None: return []
    results = [[tree]]
    depth = 0
    while depth < len(results):
        for i in range(len(results[depth])):
            if depth + 1 >= len(results) and (results[depth][i].left or results[depth][i].right):
                results.append([])            
            if results[depth][i].left: results[depth + 1].append(results[depth][i].left)
            if results[depth][i].right: results[depth + 1].append(results[depth][i].right)
            results[depth][i] = results[depth][i].data
        depth += 1
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
