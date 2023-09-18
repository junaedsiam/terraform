from queue import LifoQueue
"""
Problem description: 
---------

"""


class Queue:
    def __init__(self):
        self.stack = LifoQueue()

    def push(self, item):
        n = self.stack.qsize()
        self.stack.put(item)

        for _ in range(n):
            self.stack.put(self.stack.get())

    def top(self):
        return self.stack.queue[-1]

    def pop(self):
        return self.stack.get()

    def size(self):
        return self.stack.qsize()


if __name__ == '__main__':
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is ", q.pop())
    q.push(5)
    print("The top of the queue is ", q.top())
    print("The size of the queue is ", q.size())
