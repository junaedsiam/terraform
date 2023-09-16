"""
Problem description: 
---------
Implement queue using array
"""


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def top(self):
        return self.items[0] if self.size() else None

    def pop(self):
        return self.items.pop(0) if self.size() else None

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())
