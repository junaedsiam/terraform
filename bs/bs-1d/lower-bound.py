"""
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'
If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.
Consider 0-based indexing.

Examples
-----------
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 1
Explanation: Index 1 is the smallest index such that arr[1] >= x.
------------
Example 2:
Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] >= x.
----------
Example 3:
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 4
Result: 4
Explanation: All numbers in the list is smaller than x, hence the lower bound = n = 4.
"""


def lower_bound(nums, x):
    # Time complexity: O(log(n)), Space complexity: O(1)
    n = len(nums)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= x:
            ans = mid
            # Search for smaller index in the left
            high = mid - 1
        else:
            low = mid + 1
    return ans


if __name__ == '__main__':
    nums1, nums2 = ([1, 2, 2, 3], 2), ([3, 5, 8, 15, 19], 9)
    print(lower_bound(nums1[0], nums1[1]))
    print(lower_bound(nums2[0], nums2[1]))
