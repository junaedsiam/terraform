"""
Problem description: 
---------
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import defaultdict


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


def right_side_view(root):
    if not root:
        return []

    q = [[root, 0]]
    mp = defaultdict(lambda: None)

    while q:
        node, height = q.pop()

        if mp[height] == None:
            mp[height] = node.val

        if node.left:
            q.append([node.left, height + 1])

        if node.right:
            q.append([node.right, height + 1])

    return list(mp.values())


if __name__ == '__main__':
    print(right_side_view(create_tree([1, 2, 3, None, 5, None, 4])))
