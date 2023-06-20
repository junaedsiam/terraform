"""
Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

Examples
Example 1:
Input Format: N = 5, array[] = {1,2,3,4,5}
Result: 0
Explanation: we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.

Example 2:
Input Format: N = 5, array[] = {5,4,3,2,1}
Result: 10
Explanation: we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.

Example 3:
Input Format: N = 5, array[] = {5,3,2,1,4}
Result: 7
Explanation: There are 7 pairs (5,1), (5,3), (5,2), (5,4),(3,2), (3,1), (2,1) and we have left 2 pairs (2,4) and (1,4) as both are not satisfy our condition. 
"""

# Brute force: Count inversion for each element of an array.
# Time complexity: O(n ^ 2), Space complexity: O(1)


def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            count += (mid - left + 1)
            right += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1
    # TODO: Have to understand this with dry run
    for i in range(low, high + 1):
        nums[i] = temp[i - low]
    return count


def count_inversion_in_array(nums, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2

    count += count_inversion_in_array(nums, low, mid)
    count += count_inversion_in_array(nums, mid + 1, high)
    count += merge(nums, low, mid, high)
    return count


if __name__ == '__main__':
    nums1, nums2, nums3 = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 3, 2, 1, 4]
    print(count_inversion_in_array(nums1, 0, len(nums1) - 1))
    print(count_inversion_in_array(nums2, 0, len(nums2) - 1))
    print(count_inversion_in_array(nums3, 0, len(nums3) - 1))
