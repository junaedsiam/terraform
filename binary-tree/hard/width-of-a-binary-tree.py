"""
Problem description: 
---------
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr):
    def solve(arr, index, n):
        if index >= n:
            return None

        root = TreeNode(arr[index])
        root.left = solve(arr, 2 * index + 1, n)
        root.right = solve(arr, 2 * index + 2, n)

        return root
    return solve(arr, 0, len(arr))


def width_of_a_binary_tree(root):
    if not root:
        return 0
    q = Queue()
    q.put((root, 0))

    ans = 0

    while not q.empty():
        curr_min = q.queue[0][1]
        left_most, right_most = None, None
        size = q.qsize()
        for i in range(size):
            curr_id = q.queue[0][1] - curr_min
            tmp = q.queue[0][0]
            # Removing the item from the queue
            q.get()

            if i == 0:
                left_most = curr_id
            if i == size - 1:
                right_most = curr_id

            if tmp.left:
                q.put((tmp.left, curr_id * 2 + 1))
            if tmp.right:
                q.put((tmp.right, curr_id * 2 + 2))

        ans = max(ans, right_most - left_most + 1)

    return ans


if __name__ == '__main__':
    print(width_of_a_binary_tree(create_tree(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])))
