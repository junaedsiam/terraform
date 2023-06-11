"""
Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.
-------------
Example 1:
Input: [100, 200, 1, 3, 2, 4]
Output: 4
Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.
--------------
Example 2:
Input: [3, 8, 5, 7, 6]
Output: 4
Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.
"""
# Brute force:
# We have to sort the array, and then find the longest sequence from the sorted array


def longest_consecutive_seq_in_array_brute_force(nums):
    # Time complexity: O(n * log n), Space complexity: O(1)
    nums.sort()
    n = len(nums)
    count = 1
    curr_count = 1
    prev = nums[0]
    for i in range(1, n):
        if nums[i] == prev + 1:
            curr_count += 1
            count = max(curr_count, count)
        else:
            curr_count = 1
        prev = nums[i]
    return count


def longest_consecutive_seq_in_array(nums):
    # Even though the solution above is space optimized, we can have a time optimized
    # solution, with some space tradeoff
    # Time complexity: O(n), Space complexity: O(1)
    ht = {}
    curr_count = count = 0
    for num in nums:
        ht[num] = True
    for num in nums:
        if num - 1 not in ht:
            curr_count = 1
            curr_num = num
            while curr_num + 1 in ht:
                curr_count += 1
                curr_num += 1
            count = max(curr_count, count)
    return count


if __name__ == '__main__':
    func = longest_consecutive_seq_in_array
    nums1, nums2, nums3 = [100, 200, 1, 3, 2, 4], [
        3, 8, 5, 7, 6], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(func(nums1))
    print(func(nums2))
    print(func(nums3))
