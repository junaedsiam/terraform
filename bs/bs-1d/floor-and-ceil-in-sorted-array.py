"""
Problem Statement: You’re given an unsorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.
-------
Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.
-------
Example 2:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
Result: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""


def find_floor(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        # The floor of x is the largest element in the array which is smaller than or equal to x
        # So we will go right to find the largest
        if nums[mid] <= target:
            ans = nums[mid]
            left = mid + 1
        else:
            right = mid - 1
    return ans


def find_ceil(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        # The ceiling of x is the smallest element in the array greater than or equal to x.
        # So we will go left to find the smallest
        if nums[mid] >= target:
            ans = nums[mid]
            right = mid - 1
        else:
            left = mid + 1
    return ans


def floor_and_ceil_in_sorted_array(nums, target):
    floor = find_floor(nums, target)
    ceil = find_ceil(nums, target)
    return floor, ceil


if __name__ == '__main__':
    nums1 = [3, 4, 4, 7, 8, 10]
    print(floor_and_ceil_in_sorted_array(nums1, 5))
    print(floor_and_ceil_in_sorted_array(nums1, 8))
