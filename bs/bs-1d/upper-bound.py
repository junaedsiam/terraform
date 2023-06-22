"""
Given a sorted array of N integers and an integer x, write a program to find the upper bound of x
The upper bound in a sorted array is the index of the first value that is greater than a given value. 
If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
We are using 0-based indexing.
Try to write a solution that runs in log(n) time complexity.
Examples
----------
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] > x.
----------
Example 2:
Input Format: N = 6, arr[] = {3,5,8,9,15,19}, x = 9
Result: 4
Explanation: Index 4 is the smallest index such that arr[4] > x.
"""


def upper_bound(nums, x):
    # Time complexity: O(log(n)), Space complexity: O(1)
    n = len(nums)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > x:
            ans = mid
            # Search for smaller index in the left
            high = mid - 1
        else:
            low = mid + 1
    return ans


if __name__ == '__main__':
    nums1, nums2 = ([1, 2, 2, 3], 2), ([3, 5, 8, 9, 15, 19], 9)
    print(upper_bound(nums1[0], nums1[1]))
    print(upper_bound(nums2[0], nums2[1]))
