"""
Problem URL: https://leetcode.com/problems/target-sum/
---------

Problem Description:
---------

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""
from collections import defaultdict


def target_sum_typical_memo(nums, target):
    def f(i, curr, target, nums, dp):
        if dp[i][curr] != 1e9:
            return dp[i][curr]

        if i == n:
            if curr == target:
                return 1
            return 0

        dp[i][curr] = f(i + 1, curr + nums[i], target, nums, dp) + \
            f(i + 1, curr - nums[i], target, nums, dp)

        return dp[i][curr]

    n = len(nums)
    dp = defaultdict(lambda: defaultdict(lambda: 1e9))
    return f(0, 0, target, nums, dp)


def target_sum_with_pos_neg_version(nums, target):
    '''
    lets analyze an example combination
    for 1,1,1,1,1 target is 1 -> -1 + -1 + 1 + 1 + 1
    in here positive partition = (1 + 1 + 1)
    negative partition = (-1 -1) or - (1 + 1)
    and their difference = target, which is same as
    partition with given difference problem
    partition with given diff gist - 
    s1, s2, d
    s1 - s2 = d
    s2 = s1 - d
    s1 + s2 = total
    s1 + s1  - d = total
    2s1 = total + d
    s1 = (total + d) / 2
    find how many ways we can acieve s2
    '''
    # def f(i, ptarget, nums):
    #     if i == 0:
    #         if nums[0] == 0 and ptarget == 0:
    #             return 2
    #         if nums[0] == ptarget or ptarget == 0:
    #             return 1
    #         return 0

    #     not_pick = f(i - 1, ptarget, nums)
    #     pick = 0
    #     if ptarget >= nums[i]:
    #         pick = f(i - 1, ptarget - nums[i], nums)

    #     return pick + not_pick

    # n = len(nums)
    # total = sum(nums)

    # if (total + target) % 2 != 0:
    #     return 0

    # s1 = (total +  target) // 2

    # return f(n - 1, s1, nums)
    # Tabulation from recursive code
    n = len(nums)
    total = sum(nums)
    # for -target. if +target is achievable so as -target.
    # but moving forward we need the absolute target to find the result
    target = abs(target)
    if (total + target) % 2 != 0:
        return 0

    s1 = (total + target) // 2
    dp = [[0] * (s1 + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    if nums[0] <= s1:
        dp[0][nums[0]] = 1

    if nums[0] == 0:
        dp[0][0] = 2

    for i in range(1, n):
        for j in range(0, s1 + 1):
            not_pick = dp[i - 1][j]
            pick = 0
            if nums[i] <= j:
                pick = dp[i - 1][j - nums[i]]

            dp[i][j] = pick + not_pick

    return dp[n - 1][s1]


if __name__ == '__main__':
    print(target_sum_with_pos_neg_version())
