"""
Problem URL: https://leetcode.com/problems/number-of-longest-increasing-subsequence
---------

Problem Description:
---------
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106

"""


from typing import List


def number_of_lis(nums: List[int]) -> int:
    '''
    Time Complexity: O(n ^ 2)
    Space Complexity: O(2 * n)
    Intuition: 
    ---
    This problem is similar as the basic LIS problem. 
    By adding a count array, we can keep track of the occurances of 
    longest increasing subsequence.
    '''
    n = len(nums)
    dp = [1] * n
    cnt = [1] * n

    for i in range(n):
        for prev_i in range(i):
            if nums[prev_i] < nums[i] and 1 + dp[prev_i] > dp[i]:
                dp[i] = 1 + dp[prev_i]
                cnt[i] = cnt[prev_i]
            elif nums[prev_i] < nums[i] and 1 + dp[prev_i] == dp[i]:
                cnt[i] += cnt[prev_i]

    max_is = max(dp)
    res = 0
    for i in range(n):
        if dp[i] == max_is:
            res += cnt[i]

    return res


if __name__ == '__main__':
    print(number_of_lis([1, 2, 4, 3, 5, 4, 7, 2]))
