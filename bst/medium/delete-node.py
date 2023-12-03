"""
Problem description: 
---------
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
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


def delete_node(root, key):
    if not root:
        return None

    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        # If missing either left / right node or both
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        # node that needs to be deleted has both left and right node
        # Have to find the candidate that will connect with the left child after deletion
        # Right smallest will be the candidate for that
        right_smallest = root.right

        while right_smallest.left:
            right_smallest = right_smallest.left

        # connect right smallest with the node's left
        right_smallest.left = root.left

        # Finally return root.right, that will be connected with the deleted node's parent
        # resulting in detaching/ deleting the node from the tree
        return root.right

    return root


if __name__ == '__main__':
    traverse_inorder(delete_node(create_bst([1, 2, 3, 4, 5, 6]), 4))
