"""
Problem description: 
---------
You have given a Binary tree of 'N' node,s where the nodes have integer values.
Your task is to return the In-Order, Pre-Order, and Post-Order traversals of the given binary tree.
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


def pre_in_post_order_in_one_traversal(root):
    in_order = []
    pre_order = []
    post_order = []

    if not root:
        return in_order, pre_order, post_order

    stack = []

    stack.append((root, 1))

    while stack:
        node, count = stack.pop()

        if count == 1:
            pre_order.append(node.val)
            stack.append((node, 2))
            if node.left:
                stack.append((node.left, 1))

        elif count == 2:
            in_order.append(node.val)
            stack.append((node, 3))
            if node.right:
                stack.append((node.right, 1))

        else:
            post_order.append(node.val)

    return in_order, pre_order, post_order


if __name__ == '__main__':
    print(pre_in_post_order_in_one_traversal(
        create_tree([1, 2, 3, 4, 5, 6, 7])))
