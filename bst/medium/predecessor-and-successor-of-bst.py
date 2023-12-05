"""
Problem description: 
---------
You have given a binary search tree of integers with 'N' nodes. You are also given 'KEY' which represents data of a node of this tree. Your task is to return the predecessor and successor of the given node in the BST.
Note: Predecessor of a node in BST is that node that will be visisted just before the given node in the inorder traversal of the tree. If the given node is visited first in the inorder traversal, then its predecessor is NULL.
Note: Successor of a node in BST is that node that will be visited immediately after the given node in the inorder traversal of the tree. If the given node is visited last in the inorder traversal, then its successor is NULL.
"""

# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def create_bst(ls):
    if not ls:
        return
    ls.sort()
    mid = len(ls) // 2
    root = TreeNode(ls[mid])

    root.left = create_bst(ls[:mid])
    root.right = create_bst(ls[mid+1:])

    return root


# Implementation
def findSuccessor(root, key):
    curr = root
    succ = -1

    while curr:
        if curr.data > key:
            succ = curr.data
            curr = curr.left
        else:
            curr = curr.right

    return succ


def findPredecessor(root, key):
    curr = root
    pre = -1
    while curr:
        if curr.data < key:
            pre = curr.data
            curr = curr.right
        else:
            curr = curr.left
    return pre


def predecessor_and_successor_of_bst(root, key):
    pre = findPredecessor(root, key)
    succ = findSuccessor(root, key)

    return pre, succ


if __name__ == '__main__':
    print(predecessor_and_successor_of_bst(
        create_bst([1, 5, 9, 13, 16, 19]), 5))
