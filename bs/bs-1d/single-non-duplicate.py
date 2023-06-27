"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
-------
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
--------
Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""


def single_non_duplicate(nums):
    low = 0
    n = len(nums)
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        is_even = mid % 2 == 0
        # If the middle index is even, repeated number should place after it
        # If the middle index is odd, repeated number should place before it.
        # If any of these rules match: repeat number exists in right
        # Else repeat number exists in left
        if (is_even and mid < n - 1 and nums[mid] == nums[mid + 1]) or\
                (not is_even and mid > 0 and nums[mid] == nums[mid - 1]):
            low = mid + 1
        else:
            high = mid - 1
    return nums[low]


if __name__ == '__main__':
    nums1, nums2, nums3 = [1, 1, 2, 3, 3, 4, 4, 8, 8], [
        3, 3, 7, 7, 10, 11, 11], [1]
    # print(single_non_duplicate(nums1))
    # print(single_non_duplicate(nums2))
    print(single_non_duplicate(nums3))
