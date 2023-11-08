"""
Problem description: 
---------
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr):
    def solve(arr, index, n):
        if index >= n:
            return None

        root = TreeNode(arr[index])
        root.left = solve(arr, 2 * index + 1, n)
        root.right = solve(arr, 2 * index + 2, n)

        return root
    return solve(arr, 0, len(arr))

# Implementation


def diameter_of_a_tree(root):
    def depth(root, diameter):
        if not root:
            return 0

        ldepth = depth(root.left, diameter)
        rdepth = depth(root.right, diameter)
        diameter[0] = max(diameter[0], ldepth + rdepth)

        return 1 + max(ldepth, rdepth)

    diameter = [0]  # This is to pass the value as reference
    depth(root, diameter)
    return diameter[0]


if __name__ == '__main__':
    print(diameter_of_a_tree(create_tree([1, 2, 3, 4, 5])))
