"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""


def max_consecutive_ones(nums):
    max_count, curr_count = 0, 0

    for i in range(len(nums)):
        if nums[i] == 0:
            max_count = max(max_count, curr_count)
            curr_count = 0
        else:
            curr_count += 1

    max_count = max(max_count, curr_count)
    return max_count


if __name__ == '__main__':
    nums1, nums2 = [1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1]
    print(max_consecutive_ones(nums1))
    print(max_consecutive_ones(nums2))
