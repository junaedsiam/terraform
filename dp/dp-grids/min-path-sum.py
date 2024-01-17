"""
Problem URL: https://leetcode.com/problems/minimum-path-sum/
---------

Problem Description:
---------

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


def min_path_sum_recursive(grid):
    # Recursion
    # Time complexity: O(2 ^ n)
    # Space complexity: O(m * n)
    m = len(grid)
    n = len(grid[0])

    def solve(grid, r, c):
        up, left = float("inf"), float("inf")
        if r == 0 and c == 0:
            return grid[r][c]
        if r > 0:
            up = grid[r][c] + solve(grid, r - 1, c)
        if c > 0:
            left = grid[r][c] + solve(grid, r, c - 1)

        return min(up, left)

    return solve(grid, m - 1, n - 1)


def min_path_sum_memo(grid):
    # Memoization
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)

    m = len(grid)
    n = len(grid[0])

    def solve(grid, r, c, dp):
        up, left = float("inf"), float("inf")
        if r == 0 and c == 0:
            return grid[r][c]
        if dp[r][c] != -1:
            return dp[r][c]
        if r > 0:
            up = grid[r][c] + solve(grid, r - 1, c, dp)
        if c > 0:
            left = grid[r][c] + solve(grid, r, c - 1, dp)

        dp[r][c] = min(up, left)

        return dp[r][c]

    dp = [[-1] * n for _ in range(m)]

    return solve(grid, m - 1, n - 1, dp)


def min_path_sum_tabulation(grid):
    # Tabulation
    # Time complexity: O(m * n)
    # Space complexty: O(m * n)
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        up, left = float("inf"), float("inf")
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                continue
            if i > 0:
                up = dp[i - 1][j]
            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = grid[i][j] + min(up, left)

    return dp[m - 1][n - 1]


def min_path_sum_spaceop(grid):
    # Space op
    # Time Complexity: O(m * n)
    # Space Complexity: O(n)
    m = len(grid)
    n = len(grid[0])
    prev = [0] * n

    for i in range(m):
        up, left = float("inf"), float("inf")
        tmp = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                tmp[j] = grid[i][j]
                continue
            if i > 0:
                up = prev[j]
            if j > 0:
                left = tmp[j - 1]

            tmp[j] = grid[i][j] + min(up, left)
        prev = tmp

    return prev[n - 1]


def min_path_sum_recursive(grid):
    # Recursion
    # Time complexity: O(2 ^ n)
    # Space complexity: O(m * n)
    m = len(grid)
    n = len(grid[0])

    def solve(grid, r, c):
        up, left = float("inf"), float("inf")
        if r == 0 and c == 0:
            return grid[r][c]
        if r > 0:
            up = grid[r][c] + solve(grid, r - 1, c)
        if c > 0:
            left = grid[r][c] + solve(grid, r, c - 1)

        return min(up, left)

    return solve(grid, m - 1, n - 1)


def min_path_sum_memo(grid):
    # Memoization
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)

    m = len(grid)
    n = len(grid[0])

    def solve(grid, r, c, dp):
        up, left = float("inf"), float("inf")
        if r == 0 and c == 0:
            return grid[r][c]
        if dp[r][c] != -1:
            return dp[r][c]
        if r > 0:
            up = grid[r][c] + solve(grid, r - 1, c, dp)
        if c > 0:
            left = grid[r][c] + solve(grid, r, c - 1, dp)

        dp[r][c] = min(up, left)

        return dp[r][c]

    dp = [[-1] * n for _ in range(m)]

    return solve(grid, m - 1, n - 1, dp)


def min_path_sum_tabulation(grid):
    # Tabulation
    # Time complexity: O(m * n)
    # Space complexty: O(m * n)
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        up, left = float("inf"), float("inf")
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                continue
            if i > 0:
                up = dp[i - 1][j]
            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = grid[i][j] + min(up, left)

    return dp[m - 1][n - 1]


def min_path_sum_spaceop(grid):
    # Space op
    # Time Complexity: O(m * n)
    # Space Complexity: O(n)
    m = len(grid)
    n = len(grid[0])
    prev = [0] * n

    for i in range(m):
        up, left = float("inf"), float("inf")
        tmp = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                tmp[j] = grid[i][j]
                continue
            if i > 0:
                up = prev[j]
            if j > 0:
                left = tmp[j - 1]

            tmp[j] = grid[i][j] + min(up, left)
        prev = tmp

    return prev[n - 1]


if __name__ == '__main__':
    print(min_path_sum_spaceop([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
