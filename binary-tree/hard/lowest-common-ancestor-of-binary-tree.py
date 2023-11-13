"""
Problem description: 
---------

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor_of_binary_tree(root, p, q):
    if not root or root == p or root == q:
        return root
    # If you can find both p and q from a certain node
    # That means that node is the lowest common ancestor
    left = lowest_common_ancestor_of_binary_tree(root.left, p, q)
    right = lowest_common_ancestor_of_binary_tree(root.right, p, q)

    if not left:
        return right
    if not right:
        return left
    # Both left and right is present, return the node
    return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(lowest_common_ancestor_of_binary_tree(
        root, root.left.left, root.left.right).val)
