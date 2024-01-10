"""
Problem URL: https://leetcode.com/problems/climbing-stairs/
---------

Problem Description:
---------
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""


# memoization
def climbing_stairs(n: int) -> int:
    # Time complexity: O(n), Space Complexity: O(n)
    def solve(n, mem):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if mem[n] != -1:
            return mem[n]

        mem[n] = solve(n - 1, mem) + solve(n - 2, mem)
        return mem[n]

    mem = [-1] * (n + 1)

    return solve(n, mem)


def climbing_stairs_tab(n: int) -> int:
    # tabulation
    # Time complexity: O(n), Space Complexity: O(n)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climbing_stairs_space_op(n):
    # Time complexity: O(n), Space Complexity: O(1)
    prev = 1
    prev2 = 1

    for _ in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr

    return prev


if __name__ == '__main__':
    func = climbing_stairs_space_op
    print(func(5))
