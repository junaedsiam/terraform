from queue import Queue
"""
Problem description: 
---------
Implement a stack using queue
"""


class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        s = self.queue.qsize()
        self.queue.put(item)
        for _ in range(s):
            self.queue.put(self.queue.get())

    def pop(self):
        return self.queue.get()

    def top(self):
        return self.queue.queue[0]

    def size(self):
        return self.queue.qsize()


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(4)
    s.push(1)
    print("Top of the stack: ", s.top())
    print("Size of the stack before removing element: ", s.size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.top())
    print("Size of the stack after removing element: ", s.size())
