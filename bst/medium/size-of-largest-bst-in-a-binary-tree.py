"""
Problem description: 
---------
You have been given a Binary Tree of 'N' nodes, where the nodes have integer values. Your task is to return the size of the largest subtree of the binary tree which is also a BST.

Example:
Given binary tree:
Explanation

In the given binary tree, subtree rooted at 2 is a BST and its size is 3.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
2 1 3 -1 -1 -1 -1
Sample Output 1:
3
Explanation for Sample 1:
In the given binary tree, subtree rooted at 2 is a BST and its size is 3.
Explanation

Sample Input 2 :
50 -1 20 -1 30 -1 40 -1 50 -1 -1
Sample Output 2:
4
Constraints :
1 <= 'N' <= 10^5
0 <= 'data' <= 10^5     

where 'N' is the number of nodes and 'data' denotes the node value of the binary tree nodes.

Time limit: 1 sec
"""

# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# Impelementation


class Prop:
    def __init__(self, size=0, min=float('inf'), max=float('-inf')):
        self.size = size
        self.min = min
        self.max = max


def solve(root):
    if not root:
        return Prop()

    lprop = solve(root.left)
    rprop = solve(root.right)

    if lprop.max < root.data and rprop.min > root.data:
        return Prop(lprop.size + rprop.size + 1, min(root.data, lprop.min), max(root.data, rprop.max))

    return Prop(max(lprop.size, rprop.size), float('-inf'), float('inf'))


def size_of_largest_bst_in_a_binary_tree(root):
    prop = solve(root)
    return prop.size


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    print(size_of_largest_bst_in_a_binary_tree(root))
