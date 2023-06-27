"""
Peak element in Array
Problem Statement: Given an array, find a peak element(print anyone, if many are found). A peak element is one such that it is either greater than or equal to its neighbours. For the first and last element, it is enough to look at its only one neighbour.

Examples:

Example 1:
Input:
 arr = {3, 5, 4, 1, 1}

Output: Peak Element is 5
Explanation:
 3 and 4 are lesser than 5, therefore 5 is a peak element (1 is also a peak element).

Example 2:
Input: arr = {2,6,3,7,8,9}
Output: Peak element is 6
Explanation: 2 and 3 are lesser than 6, therefore 6 is a peak element (9 is also a peak element)

"""


def peak_element_in_array(nums):
    low = 0
    n = len(nums)
    high = n - 1
    # Its not low<=high like other bs solution.
    # low<=high will cause overflow
    while low < high:
        mid = (low + high) // 2
        if mid == 0:
            return nums[0] if nums[0] > nums[1] else nums[1]
        if mid == n - 1:
            return nums[mid] if nums[mid] > nums[mid - 1] else nums[mid - 1]

        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return nums[mid]

        if nums[mid] <= nums[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return nums[low]


if __name__ == '__main__':
    nums1, nums2 = [3, 5, 4, 1, 1], [2, 6, 3, 7, 8, 9]
    print(peak_element_in_array(nums1))
    print(peak_element_in_array(nums2))
