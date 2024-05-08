from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    came_from = None
    while tree:
        if came_from is tree.parent:
            if tree.left:
                came_from = tree
                tree = tree.left
                continue
            else:
                came_from = None
        if came_from is tree.left:
            result.append(tree.data)
            if tree.right:
                came_from = tree
                tree = tree.right
                continue
            else:
                came_from = None
        if came_from is tree.right:
            came_from = tree
            tree = tree.parent            
    return result




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
