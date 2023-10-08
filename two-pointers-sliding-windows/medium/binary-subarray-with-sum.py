"""
Problem description: 
---------
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""
import collections


def binary_subarray_with_sum(nums, goal):
    counter = collections.Counter({0: 1})
    prefix_sum = res = 0

    for num in nums:
        prefix_sum += num
        res += counter[prefix_sum - goal]
        counter[prefix_sum] += 1

    return res


if __name__ == '__main__':
    print(binary_subarray_with_sum([1, 0, 1, 0, 1], 2))
    print(binary_subarray_with_sum([0, 0, 0, 0], 0))
