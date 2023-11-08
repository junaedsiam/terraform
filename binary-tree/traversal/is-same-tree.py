"""
Problem description: 
---------

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
