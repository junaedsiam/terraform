"""
Count Occurrences in Sorted Array
Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

Examples
Example 1:
Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation: 3 is occurring 4 times in 
the given array so it is our answer.

Example 2:
Input: N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
Output: 5
Explanation: 2 is occurring 5 times in the given array so it is our answer.
"""


def first_occurance(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ans = mid
            # Search for the smallest index for first occurance
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return ans


def last_occurance(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ans = mid
            # Search for the largest index for last occurance
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return ans


def count_occurances_in_sorted_array(nums, target):
    return last_occurance(nums, target) - first_occurance(nums, target) + 1


if __name__ == '__main__':
    nums1, nums2 = ([2, 2, 3, 3, 3, 3, 4], 3), ([1, 1, 2, 2, 2, 2, 2, 3], 2)
    print(count_occurances_in_sorted_array(nums1[0], nums1[1]))
    print(count_occurances_in_sorted_array(nums2[0], nums2[1]))
