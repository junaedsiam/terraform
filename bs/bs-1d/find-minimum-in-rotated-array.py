"""
Minimum in Rotated Sorted Array
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 
-------
Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 0
Explanation: Here, the element 0 is the minimum element in the array.
-------
Example 2:
Input Format: arr = [3,4,5,1,2]
Result: 1
Explanation: Here, the element 1 is the minimum element in the array.
"""


def find_min_in_rotated_array(nums):
    low = 0
    n = len(nums)
    high = n - 1
    min_val = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < min_val:
            min_val = nums[mid]
        # Now what ?
        if min_val >= nums[high]:
            # min val present in the right part
            low = mid + 1
        else:
            # min val present in the left side
            high = mid - 1

    return min_val


if __name__ == '__main__':
    nums1, nums2, nums3 = [4, 5, 6, 7, 0, 1, 2, 3], [
        3, 4, 5, 1, 2], [11, 13, 15, 17]
    print(find_min_in_rotated_array(nums1))
    print(find_min_in_rotated_array(nums2))
    print(find_min_in_rotated_array(nums3))
