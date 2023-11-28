"""
Problem description: 
---------
Find the floor and ceil node values of a given value that is present in a BST
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


def findCeil(root, x):
    ceil = -1

    while root:
        if root.val == x:
            return x  # If input is found in the tree, return it as ceil.
        elif root.val < x:
            # Move to the right subtree if input is greater than current node's data.
            root = root.right
        else:
            ceil = root.val   # Mark ceil to be current node's data.
            # Move to the left subtree to find a closer ceil value.
            root = root.left

    return ceil  # Return computed ceil value.


def findFloor(root, x):
    floor = -1
    while root:
        if root.val == x:
            return x
        elif root.val < x:
            floor = root.val
            root = root.right
        else:
            root = root.left
    return floor


if __name__ == '__main__':
    bst = create_bst([1, 2, 3, 4,  6, 7, 8, 9])
    print(findCeil(bst, 5))
    print(findFloor(bst, 5))
