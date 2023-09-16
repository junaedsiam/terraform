"""
Problem description: 
---------
Implement stack using array
"""


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def stack_using_array():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print('Stack after pushing 3,2,1', stack.size())
    print(stack.pop())
    print('Top element of the stack after popping', stack.top())
    print('stack size:', stack.size())


if __name__ == '__main__':
    stack_using_array()
