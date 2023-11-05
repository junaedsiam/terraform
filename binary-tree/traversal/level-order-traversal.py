"""
Problem description: 
---------
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
# Helper codes


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


# Main code starts
def level_order_traversal(root):
    # Time complexity: O(n)
    if not root:
        return []
    ans, level = [], [root]

    while level:
        ans.append([node.val for node in level])

        temp = []

        for node in level:
            temp.extend([node.left, node.right])

        level = [leaf for leaf in temp if leaf]

    return ans


if __name__ == '__main__':
    print(level_order_traversal(create_tree([1, 2, 3, 4, 5, 6, 7])))
