"""
Problem description: 
---------
You are given an arbitrary binary tree consisting of 'N' nodes numbered from 1 to 'N'. Your task is to print all the root to leaf paths of the binary tree. A leaf of a binary tree is the node which does not have a left child and a right child.
Sample Input 1 :
5
1 2 3 4 5 -1 -1 -1 -1 -1 -1
Sample Output 1 :
1 2 4
1 2 5 
1 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
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


def all_root_to_leaf_paths(root):
    def solve(paths, path, node):
        path.append(node.data)

        if not node.left and not node.right:
            paths.append(" ".join([str(val) for val in path]))
            return

        if node.left:
            solve(paths, path.copy(), node.left)
        if node.right:
            solve(paths, path.copy(), node.right)

    paths = []
    solve(paths, [], root)
    return paths


if __name__ == '__main__':
    print(all_root_to_leaf_paths(create_tree([1, 2, 3, 4, 5, 6, 7, 8])))
