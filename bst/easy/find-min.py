"""
Problem description: 
---------
You are given a BST. Find the minimum value from it
"""
# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bst(ls):
    if not ls:
        return
    ls.sort()
    mid = len(ls) // 2
    root = TreeNode(ls[mid])

    root.left = create_bst(ls[:mid])
    root.right = create_bst(ls[mid+1:])

    return root

# Implementation


def find_min(root):
    min_val = -1

    while root:
        min_val = root.val
        root = root.left

    return min_val


if __name__ == '__main__':
    print(find_min(create_bst([1, 2, 3, 4, 5, 6])))
