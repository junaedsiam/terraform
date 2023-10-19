"""
Problem description: 
---------
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


from collections import Counter
import heapq


def top_k_frequent_elements(nums, k):
    # Time complexity: O(n log n)
    ct = Counter(nums)
    q = []

    for _ in range(k):
        elem, count = ct.popitem()
        heapq.heappush(q, (count, elem))

    while ct.total():
        elem, count = ct.popitem()
        heapq.heappushpop(q, (count, elem))

    return [elem for _, elem in q]


def top_k_frequent_elements_optimized(nums, k):
    # Time complexity: O(n)
    bucket = [None] * (len(nums) + 1)
    ct = Counter(nums)

    for key, freq in ct.items():
        if freq not in bucket:
            bucket[freq] = []

        bucket[freq].append(key)

    res = []

    for i in range(len(nums) - 1, -1, -1):
        if bucket[i]:
            res.extend(bucket[i])
            if len(res) >= k:
                break
    return res


if __name__ == '__main__':
    print(top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent_elements_optimized([1, 1, 1, 2, 2, 3], 2))
