"""
Problem description: 
---------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
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


def maximum_path_sum(root):
    def solve(root, max_sum):
        if not root:
            return 0
        lsum = max(0, solve(root.left, max_sum))
        rsum = max(0, solve(root.right, max_sum))
        max_sum[0] = max(max_sum[0], root.val + lsum + rsum)
        return root.val + max(lsum, rsum)
    if not root:
        return None

    max_sum = [root.val]
    solve(root, max_sum)
    return max_sum[0]


if __name__ == '__main__':
    print(maximum_path_sum(create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
