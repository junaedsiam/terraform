"""
Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 
Example 1:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

Example 2:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Result: False
Explanation: The element 10 is not present in the array. So, the answer is False.
"""


def search_in_rotated_sorted_array(nums, target):
    # Optimal: We will binary search.

    left = 0
    n = len(nums)
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        # If we think about the effect of duplicate values, it can only effect the search
        # If the same element is present at the start, end and in the middle pointers,
        # its not possible to identify the rotation and seach accordingly
        # edge case:
        if nums[mid] == nums[left] and nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue
        # mid is in sorted position
        if nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


if __name__ == '__main__':
    nums1 = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    print(search_in_rotated_sorted_array(nums1, 3))
    print(search_in_rotated_sorted_array(nums1, 10))
