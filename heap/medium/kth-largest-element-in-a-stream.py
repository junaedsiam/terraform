"""
Problem description: 
---------
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 
"""
from heapq import heappush, heapify, heappushpop, heappop
from typing import List


class KthLargest:
    # Key is to always put the kth largest element in the queue. If
    # length exceeds k, pop out the smallest elements
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums[:min(k, len(nums))]
        heapify(self.pq)

        for i in range(k, len(nums)):
            heappushpop(self.pq, nums[i])

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))
