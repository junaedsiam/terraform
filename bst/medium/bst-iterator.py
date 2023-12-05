"""
Problem description: 
---------
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""
# Helpers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bst(ls):
    if not ls:
        return
    ls.sort()
    mid = len(ls) // 2
    root = TreeNode(ls[mid])

    root.left = create_bst(ls[:mid])
    root.right = create_bst(ls[mid+1:])

    return root

# Implementation


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push(root)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.push(node.right)

        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def push(self, root):
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left


if __name__ == '__main__':
    root = create_bst([1, 2, 3, 4, 5, 6, 7])
    obj = BSTIterator(root)
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
