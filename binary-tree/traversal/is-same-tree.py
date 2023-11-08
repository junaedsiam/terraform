"""
Problem description: 
---------
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
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


def is_same_tree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right):
        return True
    return False


if __name__ == '__main__':
    print(is_same_tree(create_tree(
        [1, 2, 3, 4, 5, 6]), create_tree([1, 2, 3, 4, 5, 6])))
