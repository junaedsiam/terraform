"""
Problem description: 
---------

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


def max_depth_of_binary_tree(root, depth=0):
    if not root:
        return depth

    ldepth = max_depth_of_binary_tree(root.left, depth + 1)
    rdepth = max_depth_of_binary_tree(root.right, depth + 1)

    return max(ldepth, rdepth)


if __name__ == '__main__':
    print(max_depth_of_binary_tree(create_tree([1, 2, 3, 4, 5, 6, 7])))
