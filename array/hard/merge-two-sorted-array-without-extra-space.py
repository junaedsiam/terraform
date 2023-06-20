"""
Merge two Sorted Arrays Without Extra Space
Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
------------
Example 1:
Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]
Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]

Explanation:
After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.
-------------
Example2:
Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two non-decreasing arrays, we get, 0 1 2 3 5 6 7 8 9.
"""


def merge_two_sorted_array_without_extra_space(nums1, nums2):
    n = len(nums1)
    m = len(nums2)

    left = n - 1
    right = 0

    while left >= 0 and right < m:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break
    nums1.sort()
    nums2.sort()


if __name__ == '__main__':
    nums1, nums2 = ([1, 4, 8, 10], [2, 3, 9]), ([1, 3, 5, 7], [0, 2, 6, 8, 9])
    merge_two_sorted_array_without_extra_space(nums1[0], nums1[1])
    print(nums1)
    merge_two_sorted_array_without_extra_space(nums2[0], nums2[1])
    print(nums2)
