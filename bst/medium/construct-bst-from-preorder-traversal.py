"""
Problem description: 
---------
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

 

Example 1:


Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]
 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.

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


def solve(preorder, idx, lb, ub):
    # Edge case 1: we have reached the end
    id = idx[0]
    if id == len(preorder):
        return None

    val = preorder[id]
    # Edge case 2: current item is not suitable for BST formation
    if val < lb or val > ub:
        return None

    root = TreeNode(val)
    idx[0] = id + 1
    root.left = solve(preorder, idx, lb, val)
    root.right = solve(preorder, idx, val, ub)

    return root


def construct_bst_from_preorder_traversal(preorder):
    idx = [0]
    return solve(preorder, idx, float('-inf'), float('inf'))


if __name__ == '__main__':
    traverse_inorder(
        construct_bst_from_preorder_traversal([8, 5, 1, 7, 10, 12]))
