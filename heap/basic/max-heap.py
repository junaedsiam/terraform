
"""
Problem description: 
---------
Implement Max Heap - https://www.geeksforgeeks.org/heap-data-structure/
"""


class MaxHeap:
    def __init__(self):
        # Constructor
        self.heap = []

    def extractMaxElement(self):
        # Implement the function to remove the minimum element
        # first element of the heap is minimum.
        if not self.heap:
            return -1
        # record it
        item = self.heap[0]

        # pop the last element and insert it on top
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # heapify
        self.__heapify()

        return item

    def deleteElement(self, ind):
        # Implement the function to delete an element
        if not len(self.heap) or ind >= len(self.heap):
            return -1
        self.heap.pop(ind)
        # heapify
        self.__heapify()

    def insert(self, val):
        # Implement the function to insert 'val' in the heap
        # Insert the value at the end of the heap
        self.heap.append(val)
        # heapify
        self.__heapify()

    def __heapify(self):
        n = len(self.heap)

        for i in range(n // 2 - 1, -1, -1):
            self.__hr(i)

    def __hr(self, index):
        n = len(self.heap)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        candidate = index

        if left_child < n and self.heap[left_child] > self.heap[candidate]:
            candidate = left_child
        if right_child < n and self.heap[right_child] > self.heap[candidate]:
            candidate = right_child

        if candidate != index:
            self.heap[index], self.heap[candidate] = self.heap[candidate], self.heap[index]
            self.__hr(candidate)


if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)

    print(heap.heap)
