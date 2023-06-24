"""
Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

Note: Consider 0 based indexing

Examples:

Example 1:
Input: N = 7, target=13, array[] = {3,4,13,13,13,20,40}
Output: 4
Explanation: As the target value is 13 , it appears for the first time at index number 2.

Example 2:
Input: N = 7, target=60, array[] = {3,4,13,13,13,20,40}
Output: -1
Explanation: Target value 60 is not present in the array 
"""


def last_occurance_in_a_sorted_array(nums, target):
    n = len(nums)
    ans = -1
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ans = mid
            left = mid + 1
        elif nums[mid] > target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


if __name__ == '__main__':
    nums1 = [3, 4, 13, 13, 13, 20, 40]
    print(last_occurance_in_a_sorted_array(nums1, 13))
    print(last_occurance_in_a_sorted_array(nums1, 60))
