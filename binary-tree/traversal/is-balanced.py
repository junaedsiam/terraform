"""
Problem description: 
---------
Given a binary tree, determine if it is 
height-balanced

Example 1:
-----
Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2
---
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:
----
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


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


def height(self, root, depth=0):
    if not root:
        return depth
    ldepth = self.height(root.left, depth + 1)
    rdepth = self.height(root.right, depth + 1)
    return max(ldepth, rdepth)


def is_balanced(root):
    if not root:
        return True

    if not is_balanced(root.left) or not is_balanced(root.right):
        return False

    lheight = height(root.left)
    rheight = height(root.right)

    return abs(lheight - rheight) <= 1


if __name__ == '__main__':
    print(is_balanced(create_tree([3, 9, 20, None, None, 15, 7])))
