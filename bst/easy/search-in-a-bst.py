"""
Problem description: 
---------

Topics
Companies
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""


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


def search_in_a_bst(root, val):
    while root:
        if root.val == val:
            return root

        if root.val < val:
            root = root.right
        else:
            root = root.left

    return None


if __name__ == '__main__':
    print(search_in_a_bst(create_bst([1, 2, 3, 4, 5]), 4))
    print(search_in_a_bst(create_bst([1, 2, 3, 4, 5]), 6))
