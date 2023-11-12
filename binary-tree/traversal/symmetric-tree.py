"""
Problem description: 
---------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

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


def symmetric_tree(root):
    def solve(left, right):
        if not left and not right:
            return True

        if left and right and \
                left.val == right.val and \
                solve(left.left, right.right) and solve(left.right, right.left):
            return True
        return False

    return solve(root.left, root.right)


if __name__ == '__main__':
    print(symmetric_tree(create_tree([1, 2, 2, 3, 4, 4, 3])))
