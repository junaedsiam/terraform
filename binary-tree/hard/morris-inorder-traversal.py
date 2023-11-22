"""
Problem description: 
---------
In order traversal of a binary tree but without recursion and without using stack
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
def morris_inorder_traversal(root):
    # Time complexity: O(n), Space Complexity: O(1)
    curr = root
    ans = []

    while curr:
        if not curr.left:
            ans.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left

            while prev.right and prev.right != curr:
                prev = prev.right

            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                ans.append(curr.val)
                curr = curr.right

    return ans


if __name__ == '__main__':
    print(morris_inorder_traversal(create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])))
