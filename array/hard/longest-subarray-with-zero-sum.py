"""
Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
Example 1:
Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result: 5
Explanation: The following subarrays sum to zero:
{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
Since we require the length of the longest subarray, our answer is 5!
-----------------
Example 2:
Input Format: N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}
Result: 8
Subarrays with sum 0 : {-2, 2}, {-8, 1, 7}, {-2, 2, -8, 1, 7}, {6, -2, 2, -8, 1, 7, 4, -10}
Length of longest subarray = 8
-------------------
Example 3:
Input Format: N = 3, array[] = {1, 0, -5}
Result: 1
Subarray : {0}
Length of longest subarray = 1
---------------
Example 4:
Input Format: N = 5, array[] = {1, 3, -5, 6, -2}
Result: 0
Subarray: There is no subarray that sums to zero
"""

# Brute force: Get all possible subarrays and their sums, track the max number of elements
# that results in zero.
# Time complexity: O(n ^ 2), Space complexity: O(1)


def longest_subarray_with_zero_sum(nums):
    # Optimal approach
    # By using a hashmap, and traversing the array once
    # Time complexity: O(n), Space complexity: O(n)
    n = len(nums)
    max_len = 0
    hl = {}
    sum = 0
    for i in range(n):
        sum += nums[i]
        if sum == 0:
            max_len = i + 1
        else:
            if sum in hl:
                max_len = max(max_len, i - hl[sum])
            else:
                hl[sum] = i
    return max_len


if __name__ == '__main__':
    nums1, nums2, nums3, nums4 = [
        9, -3, 3, -1, 6, -5], [6, -2, 2, -8, 1, 7, 4, -10], [1, 0, -5], [1, 3, -5, 6, -2]
    print(longest_subarray_with_zero_sum(nums1))
    print(longest_subarray_with_zero_sum(nums2))
    print(longest_subarray_with_zero_sum(nums3))
    print(longest_subarray_with_zero_sum(nums4))
