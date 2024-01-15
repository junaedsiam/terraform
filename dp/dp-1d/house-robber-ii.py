"""
Problem URL: https://leetcode.com/problems/house-robber-ii/description/
---------

Problem Description:
---------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

"""


from typing import List


def solve(nums: List[int]) -> int:
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


def house_robber_ii(nums: List[int]) -> int:
    # This is similar to the House robber 1 problem, except
    # here the neighboring houses are in circle.
    # That means if you rob the first house, you cannot rob
    # the last house as they are neighbor in a circle.
    # --
    # We could use robber 1 solution here too
    # res1: run the robber 1 solution on the list without the first element
    # res2: run the robber 1 solution without the last element
    # return max(res1, res2)
    # Time complexity: O(n)

    if len(nums) == 1:
        return nums[0]

    res1 = solve(nums[:-1])
    res2 = solve(nums[1:])

    return max(res1, res2)


if __name__ == '__main__':
    print(house_robber_ii([1, 2, 3, 1]))
