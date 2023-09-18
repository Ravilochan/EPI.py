from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# with recursive traversal
def inorder_r_traversal(tree: BinaryTreeNode) -> List[int]:
    def inorder(node: BinaryTreeNode, path: List[int]):
        if node:
            inorder(node.left, path)
            path.append(node.data)
            inorder(node.right, path)
    order = []
    inorder(tree, order)
    return order


# with iterative traversal
def inorder_i_traversal(tree: BinaryTreeNode) -> List[int]:
    stack, path = [], []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            path.append(tree.data)
            tree = tree.right
    return path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_i_traversal))

# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
#                                        inorder_r_traversal))
