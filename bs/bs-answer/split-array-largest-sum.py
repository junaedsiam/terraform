"""
Problem description: 
---------
Given an integer array 'A' of size 'N' and an integer 'K'. Split the array 'A' into 'K' non-empty subarrays such that the largest sum of any subarray is minimized. Your task is to return the minimized largest sum of the split.
A subarray is a contiguous part of the array.
Example 1:
Input Format: N = 5, a[] = {1,2,3,4,5}, k = 3
Result: 6
Explanation: There are many ways to split the array a[] into k consecutive subarrays. The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

Example 2:
Input Format: N = 3, a[] = {3,5,1}, k = 3
Result: 5
Explanation: There is only one way to split the array a[] into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.
"""


def get_split_amount(nums, sum, k):
    n = len(nums)
    k_count = 1
    curr_sum = 0
    for i in range(n):
        if curr_sum + nums[i] <= sum:
            curr_sum += nums[i]
        else:
            k_count += 1
            curr_sum = nums[i]
    return k_count


def split_array_largest_sum(nums, k):
    # Time complexity: O (n * log (m))
    n = len(nums)

    if n < k:
        return -1

    low = max(nums)
    high = sum(nums)

    while low <= high:
        mid = (low + high) // 2
        if get_split_amount(nums, mid, k) > k:
            low = mid + 1
        else:
            high = mid - 1
    return low


if __name__ == '__main__':
    ex_1, ex_2 = ([1, 2, 3, 4, 5], 3), ([3, 5, 1], 3)
    print(split_array_largest_sum(ex_1[0], ex_1[1]))
    print(split_array_largest_sum(ex_2[0], ex_2[1]))
