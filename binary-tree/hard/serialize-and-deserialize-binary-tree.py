"""
Problem description: 
---------
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
from collections import deque

# Helpers


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(arr):
    def solve(arr, index, n):
        if index >= n:
            return None

        root = TreeNode(arr[index])
        root.left = solve(arr, 2 * index + 1, n)
        root.right = solve(arr, 2 * index + 2, n)

        return root
    return solve(arr, 0, len(arr))


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

# Implementation


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q = deque([root])
        res = ""

        while len(q):
            res += "," if res else ""
            node = q.popleft()
            if not node:
                res += "#"
            else:
                res += str(node.val)
                q.append(node.left)
                q.append(node.right)

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        ls = data.split(",")

        root = TreeNode(ls[0])
        q = deque([root])
        i = 1

        while i < len(ls):
            node = q.popleft() if q else None

            if ls[i] != '#':
                left = TreeNode(int(ls[i]))
                node.left = left
                q.append(left)
            i += 1
            if i < len(ls) and ls[i] != '#':
                right = TreeNode(int(ls[i]))
                node.right = right
                q.append(right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(create_tree([1, 2, 3, 4, 5, 6])))
    print(level_order_traversal(ans))
