"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

# Time complexity: O(n), Space complexity: O(d)


def left_rotate_by_d_place(nums, d):
    n = len(nums)
    d = d % n
    d_arr = [0] * d

    for i in range(d):
        d_arr[i] = nums[i]

    for i in range(d, n):
        nums[i - d] = nums[i]

    for i in range(d):
        nums[n - d + i] = d_arr[i]


# Rotation with space optimization
"""
d = 2
Step 1: reverse 0 to d - 1
Step 2: reverse d to n - 1
Step 3: reverse the whole array
"""


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Time complexity: O(n), Space complexity: O(1)


def left_rotate_by_d_place_optimal(nums, d):
    n = len(nums)
    d = d % n
    reverse(nums, 0, d - 1)
    reverse(nums, d, n - 1)
    reverse(nums, 0, n - 1)


if __name__ == '__main__':
    nums1, nums2, nums3 = ([3, 7, 8, 9, 10, 11], 2), ([
        1, 2, 3, 4, 5, 6, 7], 3), ([-1, -100, 3, 99], 2)

    func = left_rotate_by_d_place_optimal

    func(nums1[0], nums1[1])
    print(nums1[0])
    func(nums2[0], nums2[1])
    print(nums2[0])
    func(nums3[0], nums3[1])
    print(nums3[0])
