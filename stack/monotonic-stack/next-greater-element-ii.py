"""
Problem description: 
---------
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.


Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""


def next_greater_element_ii_brute_force(nums: int):
    # Time complexity: O(n ^ 2), Space Complexity: O(n)
    n = len(nums)
    nums = nums * 2  # This replicates the list and attach the replica with the original one
    res = []
    for i in range(n):
        ans = -1
        for j in range(i + 1, i + n):
            if nums[j] > nums[i]:
                ans = nums[j]
                break
        res.append(ans)

    return res


def next_greater_element_ii(nums):
    # Time complexity: O(n), Space complexity: O(n)
    stack = []
    res = [-1] * len(nums)
    for _ in range(2):
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
    return res


if __name__ == '__main__':
    print(next_greater_element_ii_brute_force([1, 2, 1]))
    print(next_greater_element_ii_brute_force([1, 2, 3, 4, 3]))
    print(next_greater_element_ii([1, 2, 1]))
    print(next_greater_element_ii([1, 2, 3, 4, 3]))
