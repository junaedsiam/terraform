"""
Problem description: 
---------
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
# General observations
# - nums[i] can be negative.


def count_all_subsequences_with_sum_k(nums, k):
    # Brute force:
    # Initiate with a counter variable.
    # Generate all possible subarrays and their sum. If the sum == k increase the counter by 1
    # Finally return the counter
    # Time complexity: O(n ^ 2), Space complexity: O(1)
    count = 0
    for i in range(len(nums)):
        sum = nums[i]
        if sum == k:
            count += 1
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            if sum == k:
                count += 1
    return count


def count_all_subsequences_with_sum_k_optimized(nums, k):
    # using hashmap
    # Time Complexity: O(n), Space complexity: O(n)
    ht = {0: 1}
    count = 0
    sum = 0
    for num in nums:
        sum += num
        if sum - k in ht:
            count += ht[sum - k]
        if sum in ht:
            ht[sum] += 1
        else:
            ht[sum] = 1
    return count


if __name__ == '__main__':
    func = count_all_subsequences_with_sum_k_optimized
    print(func([1, 1, 1], 2))
    print(func([1, 2, 3], 3))
    print(func([1, 1, 1], 1))
    print(func([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))
