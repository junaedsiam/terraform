"""
Problem URL: https://leetcode.com/problems/longest-increasing-subsequence/
---------

Problem Description:
---------

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
"""

from typing import List


def lis_memo(nums: List[int]) -> int:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n ^ 2)
    def solve(i, prev_i, nums, dp):
        # base case
        if i == len(nums):
            return 0
        if dp[i][prev_i] != -1:
            return dp[i][prev_i]

        not_take = solve(i + 1, prev_i, nums, dp)
        take = 0
        if prev_i == -1 or nums[i] > nums[prev_i]:
            take = 1 + solve(i + 1, i, nums, dp)

        dp[i][prev_i] = max(take, not_take)
        return dp[i][prev_i]

    n = len(nums)
    dp = [[-1] * n for _ in range(n)]
    return solve(0, -1, nums, dp)


def lis_tabulation(nums: List[int]) -> int:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    # ---
    # This is a bit different approach of tabulation than what we have been doing so far.
    # Idea is one loop will iterate over all the numbers
    # second nested will iterate throught the prev numbers
    # which is 0 to i - 1, where i is current index
    # inside that second loop, we will check for the prev numbers which are smaller than
    # current one, if found, we will take the lis from recorded dp for that prev index
    # dp[i] = dp[prev_i] + 1 if dp[prev_i] + 1 > dp[i], which by default is 1
    # --
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for prev_i in range(i):
            if nums[prev_i] < nums[i] and 1 + dp[prev_i] > dp[i]:
                dp[i] = 1 + dp[prev_i]

    return max(dp)


def lis_print_tabulation(nums):
    # In this case, requirement is to print the subseq
    n = len(nums)
    dp = [1] * n
    pts = [0] * n
    for i in range(n):
        pts[i] = i
        for prev_i in range(i):
            if nums[prev_i] < nums[i] and 1 + dp[prev_i] > dp[i]:
                dp[i] = 1 + dp[prev_i]
                pts[i] = prev_i

    end = 0

    for i in range(n):
        if dp[i] > dp[end]:
            end = i

    curr = end
    res = []
    while dp[curr] != 1:
        res.append(nums[curr])
        curr = pts[curr]

    res.append(nums[curr])

    res.reverse()

    return res


if __name__ == '__main__':
    print(lis_memo([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lis_tabulation([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lis_print_tabulation([10, 9, 2, 5, 3, 7, 101, 18]))
