"""
Problem description: 
---------
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_complete_tree_nodes(root):
    # Time complexity: O(log ^ 2(n))
    if not root:
        return 0

    hl, hr = 0, 0
    l, r = root, root

    while l:
        hl += 1
        l = l.left

    while r:
        hr += 1
        r = r.right

    if hl == hr:
        return 2 ** hl - 1

    return 1 + count_complete_tree_nodes(root.left) + count_complete_tree_nodes(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(count_complete_tree_nodes(root))
