"""
Problem description: 
---------
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

"""
# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    # Time complexity: O(n)
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

# Implementations


def solve(preorder, pre_start, pre_end, inorder, in_start, in_end, mp):
    if pre_start > pre_end or in_start > in_end:
        return None

    node = TreeNode(preorder[pre_start])
    pivot_index = mp[preorder[pre_start]]
    elem_count = pivot_index - in_start

    node.left = solve(preorder, pre_start + 1, pre_start +
                      elem_count, inorder, in_start, pivot_index - 1, mp)
    node.right = solve(
        preorder, pre_start + elem_count + 1, pre_end, inorder, pivot_index + 1, in_end, mp)

    return node


def construct_binary_tree_from_inorder_preorder(preorder, inorder):
    # Create a map from inorder
    mp = {inorder[i]: i for i in range(len(inorder))}
    # define pre_start, pre_end, in_start, in_end
    pre_start, pre_end = 0, len(preorder) - 1
    in_start, in_end = 0, len(inorder) - 1
    # recursively build the tree from both traversal output
    return solve(preorder, pre_start, pre_end, inorder, in_start, in_end, mp)


if __name__ == '__main__':
    print(level_order_traversal(construct_binary_tree_from_inorder_preorder(
        [3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
