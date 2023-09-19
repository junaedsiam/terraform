"""
Problem description: 
---------
Implement a min stack with push, pop, top and getMin methods. Each of the operation must take O(1) time
"""


class Node:
    def __init__(self, val, minimum, next=None):
        self.val = val
        self.min = minimum
        self.next = next


class MinStack:
    def __init__(self):
        self.node = None

    def push(self, val: int) -> None:
        if not self.node:
            self.node = Node(val, val)
        else:
            self.node = Node(val, min(self.node.min, val), self.node)

    def pop(self) -> None:
        self.node = self.node.next

    def top(self) -> int:
        return self.node.val

    def getMin(self) -> int:
        return self.node.min


if __name__ == '__main__':
    stack = MinStack()
    stack.push(40)
    stack.push(10)
    stack.push(2)
    stack.push(5)
    print('Stack top', stack.top())
    print('Stack min', stack.getMin())
    print('Stack pop', stack.pop())
    print('Stack pop', stack.pop())
    print('Stack min after 2 pop operations', stack.getMin())
