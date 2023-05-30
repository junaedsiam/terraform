"""
Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
"""

# Brute force
# Try all combinations to get the k, and return the longest count

# Better approach
# Use a little bit complex hashing algorithm, which is optimal if the array contains negative value.
# And we will ofcourser revisit it later


def longest_subarray(nums, k):
    # Optimal approach
    # # Two pointer
    n = len(nums)
    left, right = 0, 0
    sum = 0
    max_len = 0
    while right < n:
        sum += nums[right]
        # sum is equal to k
        if sum == k:
            max_len = max(max_len, right - left + 1)
        # sum is greather than k
        elif sum > k:
            sum -= nums[left]
            left += 1

        right += 1
        # sum is less than k
    return max_len


if __name__ == '__main__':
    nums1, nums2 = [[2, 3, 5, 1, 9], 10], [[2, 3, 5], 5]
    print(longest_subarray(nums1[0], nums1[1]))
    print(longest_subarray(nums2[0], nums2[1]))
