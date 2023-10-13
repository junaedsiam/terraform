"""
Problem description: 
---------
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import heapq


def kth_largest_element(nums, k):
    h = []
    for num in nums:
        heapq.heappush(h, -num)

    for _ in range(k - 1):
        heapq.heappop(h)

    return -h[0]


if __name__ == '__main__':
    print(kth_largest_element())
