"""
Problem description: 
---------
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""

from collections import defaultdict
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def track_parents(pmap, root):
    q = Queue()
    q.put(root)
    pmap[root] = None

    while not q.empty():
        node = q.get()
        if node.left:
            pmap[node.left] = node
            q.put(node.left)
        if node.right:
            pmap[node.right] = node
            q.put(node.right)


def all_nodes_with_distance_k_binary_tree(root, target, k):
    # Step 1: record parent for each node with a hash map
    pmap = defaultdict(lambda: None)
    track_parents(pmap, root)
    # Step 2: take a map to track visited node
    visited = defaultdict(lambda: False)
    visited[target] = True
    curr_k = 0
    q = Queue()
    q.put(target)
    # Step 3: now from k node go k distance to find the nodes that are k distance away
    while not q.empty():
        if curr_k == k:
            break
        curr_k += 1
        size = q.qsize()
        for i in range(size):
            curr = q.get()
            # go left
            if curr.left and not visited[curr.left]:
                visited[curr.left] = True
                q.put(curr.left)
            # go right
            if curr.right and not visited[curr.right]:
                visited[curr.right] = True
                q.put(curr.right)
            if pmap[curr] and not visited[pmap[curr]]:
                visited[pmap[curr]] = True
                q.put(pmap[curr])
    ans = []

    while not q.empty():
        node = q.get()
        ans.append(node.val)

    return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(all_nodes_with_distance_k_binary_tree(root, root.left, 2))
