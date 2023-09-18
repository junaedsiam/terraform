"""
Problem description: 
---------
Implement stack using a linked list
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Stack:
    def __init__(self):
        self.list = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return bool(self.size)

    def push(self, data):
        node = Node(data)
        self.size += 1
        if self.list:
            prev = self.list
            node.next = prev

        self.list = node

    def pop(self):
        item = None
        if self.size:
            item = self.list.data
            self.size -= 1
            self.list = self.list.next
        return item

    def getTop(self):
        if self.size:
            return self.list.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('Top of the stack is:', stack.getTop())
    print('Size of the stack is:', stack.size)
    print('Popped element from the stack is:', stack.pop())
    print('Stack size after popping:', stack.size)
