"""
Problem description: 
---------
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
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


def inorder(root, ls):
    if not root:
        return
    inorder(root.left, ls)
    ls.append(root.val)
    inorder(root.right, ls)


def two_sum_in_bst(root, k):
    # inorder traversal will give sorted list
    ls = []
    inorder(root, ls)
    # Apply two pointer on the sorted list to find out two sum
    l = 0
    r = len(ls) - 1

    while l < r:
        total = ls[l] + ls[r]
        if total == k:
            return True

        if total > k:
            r -= 1
        else:
            l += 1

    return False


if __name__ == '__main__':
    print(two_sum_in_bst(create_bst([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10))
    print(two_sum_in_bst(create_bst([1, 2, 3, 4, 5, 6, 7, 8, 9]), 30))
