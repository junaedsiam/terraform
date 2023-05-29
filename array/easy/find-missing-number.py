"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""

"""
If we xor same number, that results in 0
so 1 ^ 1 = 0
similarly 1 ^ 1 ^ 2 ^ 2 = 0
but 1 ^ 1 ^ 2 ^ 2 ^ 3 = 3
So if we iterate through nums and xor both i and nums[i], we will find the missing number at the end
"""


def find_missing_number(nums):
    n = len(nums)
    res = n
    for i in range(n):
        res ^= nums[i]
        res ^= i
    return res


if __name__ == '__main__':
    nums1, nums2, nums3 = [3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(find_missing_number(nums1))
    print(find_missing_number(nums2))
    print(find_missing_number(nums3))
