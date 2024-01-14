"""
Problem URL: https://leetcode.com/problems/house-robber/
---------

Problem Description:
---------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400


"""
from typing import List


def house_robber_recurse(nums: List[int]) -> int:
    # recursion
    # Time complexity: O(2 ^ n)
    def solve(idx, nums):
        # negative index, return 0
        if idx < 0:
            return 0
        # If idx reaches 0th index, that means 1 has not been taken
        # return the value of 0th index
        if idx == 0:
            return nums[idx]

        pick = nums[idx] + solve(idx - 2, nums)
        notPick = 0 + solve(idx - 1, nums)

        return max(pick, notPick)

    return solve(len(nums) - 1, nums)


def house_robber_memoization(nums: list[int]) -> int:
    # memoization
    # Time complexity: O(n)
    # Space complexity: O(n)
    def solve(idx, nums, dp):
        # negative index, return 0
        if idx < 0:
            return 0
        # If idx reaches 0th index, that means 1 has not been taken
        # return the value of 0th index
        if idx == 0:
            return nums[idx]

        pick = nums[idx] + solve(idx - 2, nums, dp)
        notPick = 0 + solve(idx - 1, nums, dp)

        return max(pick, notPick)

    n = len(nums)
    dp = [-1] * n

    return solve(len(nums) - 1, nums, dp)


def house_robber_tabulation(nums: List[int]) -> int:
    # Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        pick = nums[i]
        if i > 1:
            pick += dp[i - 2]

        notPick = dp[i - 1]

        dp[i] = max(pick, notPick)

    return dp[n - 1]


def house_robber_spaceop(nums: List[int]) -> int:
    # Space Op
    # Time complexity: O(n)
    # Space complexity: 0(1)
    n = len(nums)
    prev2 = 0
    prev1 = nums[0]

    for i in range(1, n):
        pick = nums[i] + prev2
        notPick = prev1

        curri = max(pick, notPick)
        prev2 = prev1
        prev1 = curri

    return prev1


if __name__ == '__main__':
    func = house_robber_spaceop
    print(func([2, 7, 9, 3, 1]))
