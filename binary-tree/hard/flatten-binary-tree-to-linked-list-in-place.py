"""
Problem description: 
---------
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

"""
prev = None


def flatten_binary_tree_to_linked_list_in_place(root):
    global prev
    if not root:
        return

    flatten_binary_tree_to_linked_list_in_place(root.right)
    flatten_binary_tree_to_linked_list_in_place(root.left)

    root.right = prev
    root.left = None
    prev = root


if __name__ == '__main__':
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

    root = create_tree([1, 2, 3, 4, 5, 6])

    flatten_binary_tree_to_linked_list_in_place(root)

    while root:
        print(root.val, end=", ")
        root = root.right
