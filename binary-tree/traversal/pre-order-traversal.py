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


def pre_order_traversal(root):
    # Iterative Approach
    # Time complexity:
    if not root:
        return []

    res = []
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return res


def pre_order_traversal_recursive(root):
    # Recursive Approach
    def preorder(root, ls):
        if not root:
            return
        ls.append(root.val)
        preorder(root.left, ls)
        preorder(root.right, ls)

    ls = []
    preorder(root, ls)
    return ls


if __name__ == '__main__':
    print(pre_order_traversal(create_tree([1, 2, 3, 4, 5, 6, 7])))
    print(pre_order_traversal_recursive(create_tree([1, 2, 3, 4, 5, 6, 7])))
