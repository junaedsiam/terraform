"""
Problem description: 
---------
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""

# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_inorder(root):
    if not root:
        return
    traverse_inorder(root.left)
    print(root.val, end=",")
    traverse_inorder(root.right)

# Implementation


prev = TreeNode(float('-inf'))
first = None
middle = None
last = None


def swap(node1, node2):
    tmp = node1.val
    node1.val = node2.val
    node2.val = tmp


def inorder(root):
    global first, last, middle, prev
    if not root:
        return
    inorder(root.left)
    # some operations
    if root.val < prev.val:
        if not first:
            # first element found
            first = prev
            middle = root
        else:
            last = root
            # last element found
    prev = root
    inorder(root.right)


def recover_tree(root) -> None:
    global first, last

    inorder(root)
    if first and last:
        swap(first, last)
    else:
        swap(first, middle)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    traverse_inorder(root)
    print()
    recover_tree(root)
    traverse_inorder(root)
