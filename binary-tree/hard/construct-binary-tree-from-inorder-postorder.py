"""
Problem description: 
---------
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    if not root:
        return []
    ans, level = [], [root]

    while level:
        ans.append([node.val for node in level])

        temp = []

        for node in level:
            temp.extend([node.left, node.right])

        level = [leaf for leaf in temp if leaf]

    return ans


# Implementation
def solve(inorder, in_start, in_end, postorder, post_start, post_end, mp):
    if in_start > in_end or post_end > post_start:
        return
    node = TreeNode(postorder[post_start])
    pivot = mp[postorder[post_start]]
    elem_count = in_end - pivot
    # Recursive call for left and right
    node.left = solve(inorder, in_start, pivot - 1,
                      postorder, post_start - elem_count - 1, post_end, mp)
    node.right = solve(inorder, pivot + 1, in_end,
                       postorder, post_start - 1, post_start - elem_count, mp)

    return node


def construct_binary_tree_from_inorder_postorder(inorder, postorder):
    mp = {inorder[i]: i for i in range(len(inorder))}

    in_start, in_end = 0, len(inorder) - 1
    post_start, post_end = len(postorder) - 1, 0

    return solve(inorder, in_start, in_end, postorder, post_start, post_end, mp)


if __name__ == '__main__':
    print(level_order_traversal(construct_binary_tree_from_inorder_postorder(
        [9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
