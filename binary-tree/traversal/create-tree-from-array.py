"""
Problem description: 
---------
Given a Node object, create binary tree from a given array
"""


# Iterative Method to print the
# height of a binary tree
def print_level_order(root):

    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_tree_from_array_iterative(arr):
    # Time complexity:
    n = len(arr)
    nodes = [Node(item) for item in arr]

    for i in range(n // 2):
        if (2 * i + 1) < n:
            # left child is possible
            nodes[i].left = nodes[2 * i + 1]
        if (2 * i + 2) < n:
            # right child is possible
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]


def create_tree_from_array_recursive(arr):
    def solve(arr, index, n):
        if index >= n:
            return None

        root = Node(arr[index])
        root.left = solve(arr, 2 * index + 1, n)
        root.right = solve(arr, 2 * index + 2, n)

        return root
    return solve(arr, 0, len(arr))


if __name__ == '__main__':
    func = create_tree_from_array_recursive
    print_level_order(func([1, 2, 3, 4, 5, 6, 7]))
