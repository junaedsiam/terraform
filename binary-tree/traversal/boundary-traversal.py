"""
Problem description: 
---------
Write a program for the Anti-Clockwise Boundary traversal of a binary tree.
"""
# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
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


def is_leaf(node):
    return True if (not node.left and not node.right) else False


def left_traversal(root, res):
    curr = root.left
    while curr:
        if not is_leaf(curr):
            res.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right


def leaf_traversal(root, res):
    if not root:
        return
    if is_leaf(root):
        res.append(root.data)
    leaf_traversal(root.left, res)
    leaf_traversal(root.right, res)


def right_traversal(root, res):
    tmp = []
    curr = root.right
    while curr:
        if not is_leaf(curr):
            tmp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    # For reverse entry
    for i in range(len(tmp) - 1, -1, -1):
        res.append(tmp[i])


def boundary_traversal(root):
    if not root:
        return []

    res = []
    res.append(root.data)
    # traverse left boundary
    left_traversal(root, res)
    # traverse leaf only
    leaf_traversal(root, res)
    # traverse right boundary
    right_traversal(root, res)

    return res


if __name__ == '__main__':
    print(boundary_traversal(create_tree([1, 2, 3, 4, 5, 6])))
