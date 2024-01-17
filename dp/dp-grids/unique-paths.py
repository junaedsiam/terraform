"""
Problem URL:https://leetcode.com/problems/unique-paths/ 
---------

Problem Description:
---------
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""


def unique_paths_recurse(m: int, n: int) -> int:
    # Recursion:
    # Time complexity: O(2 ^ ( m + n))
    # Space complexity: O(m + n)
    def solve(r, c):
        if r == 0 and c == 0:
            return 1
        if r == 0:
            return solve(r, c - 1)
        if c == 0:
            return solve(r - 1, c)

        return solve(r - 1, c) + solve(r, c - 1)

    return solve(m - 1, n - 1)


def unique_paths_memoize(m: int, n: int) -> int:
    # Memoization
    # Time complexity: O(m * n)
    # Space complexity: O( m * n)
    def solve(r, c, dp):
        if r == 0 and c == 0:
            return 1
        if dp[r][c] != -1:
            return dp[r][c]
        if r == 0:
            dp[r][c] = solve(r, c - 1, dp)
        elif c == 0:
            dp[r][c] = solve(r - 1, c, dp)
        else:
            dp[r][c] = solve(r - 1, c, dp) + solve(r, c - 1, dp)

        return dp[r][c]

    dp = [[-1] * n for _ in range(m)]
    return solve(m - 1, n - 1, dp)


def unique_path_tabulation(m: int, n: int) -> int:
    # Tabulation
    # Time complexity: O ( m * n)
    # SPace complexity: O(m * n)
    dp = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                dp[r][c] = 1
                continue

            up, left = 0, 0
            if r > 0:
                up = dp[r - 1][c]
            if c > 0:
                left = dp[r][c - 1]

            dp[r][c] = up + left

    return dp[m - 1][n - 1]


def unique_path_spaceop(m: int, n: int) -> int:
    # Space optimization
    # Time complexity: O(m * n)
    # Space complexity: O(n)
    prev = [0] * n

    for r in range(m):
        tmp = [0] * n
        for c in range(n):
            if r == 0 and c == 0:
                tmp[c] = 1
                continue

            up, left = 0, 0
            if r > 0:
                up = prev[c]
            if c > 0:
                left = tmp[c - 1]

            tmp[c] = up + left
        prev = tmp

    return prev[n - 1]


if __name__ == '__main__':
    func = unique_path_spaceop
    print(func(3, 7))
