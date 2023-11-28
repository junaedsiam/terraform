"""
Problem description: 
---------
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
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


def traverse_inorder(root):
    if not root:
        return
    traverse_inorder(root.left)
    print(root.val, end=",")
    traverse_inorder(root.right)

# Implementation


def insert_a_node(root, val):
    # edge case
    if not root:
        return TreeNode(val)

    if root.val < val:
        root.right = insert_a_node(root.right, val)
    elif root.val > val:
        root.left = insert_a_node(root.left, val)

    return root


if __name__ == '__main__':
    bst = create_bst([1, 6, 9, 11, 67])
    traverse_inorder(insert_a_node(bst, 5))
