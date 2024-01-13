"""
Problem URL:https://www.codingninjas.com/studio/problems/frog-jump_3621012 
---------

Problem Description:
---------

Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.
"""

from typing import List


def frog_jump_recurse(n: int, heights: List[int]) -> int:
    # Recursion
    # Time complexity: O(2 ^ n)
    def solve(idx, heights):
        if idx == 0:
            return 0
        jump1 = solve(idx - 1, heights) + abs(heights[idx] - heights[idx - 1])
        jump2 = float('inf')

        if idx > 1:
            # 2 steps jump is allowed here
            jump2 = solve(idx - 2, heights) + \
                abs(heights[idx] - heights[idx - 2])

        return min(jump2, jump1)

    return solve(n - 1, heights)


def frog_jump_memo(n: int, heights: List[int]) -> int:
    # memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    def solve(idx, heights, dp):
        if idx == 0:
            return 0

        if dp[idx] != -1:
            return dp[idx]

        jump1 = solve(idx - 1, heights, dp) + \
            abs(heights[idx] - heights[idx - 1])
        jump2 = float('inf')

        if idx > 1:
            # 2 steps jump is allowed here
            jump2 = solve(idx - 2, heights, dp) + \
                abs(heights[idx] - heights[idx - 2])

        dp[idx] = min(jump2, jump1)
        return dp[idx]

    dp = [-1] * n
    return solve(n - 1, heights, dp)


def frog_jump_tabluation(n: int, heights: List[int]) -> int:
    # Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)
    dp = [0] * n
    for i in range(1, n):
        jump1 = dp[i - 1] + abs(heights[i] - heights[i - 1])
        jump2 = float('inf')

        if i > 1:
            jump2 = dp[i - 2] + abs(heights[i] - heights[i - 2])

        dp[i] = min(jump1, jump2)

    return dp[n - 1]


def frog_jump_space_op(n, heights):
    # Space optimization
    # Time  complexity: O(n)
    # Spafe complexity: O(1)
    prev1 = 0
    prev2 = None
    for i in range(1, n):
        jump1 = prev1 + abs(heights[i] - heights[i - 1])
        jump2 = float('inf')

        if i > 1:
            jump2 = prev2 + abs(heights[i] - heights[i - 2])
        prev2 = prev1
        prev1 = min(jump1, jump2)

    return prev1


if __name__ == '__main__':
    func = frog_jump_space_op
    print(func(4, [10, 20, 30, 10]))
