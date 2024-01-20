"""
Problem URL: https://leetcode.com/problems/minimum-falling-path-sum/
---------

Problem Description:
---------
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

"""


# memoization
from typing import List


def min_fall_path_recurse(matrix: List[List[int]]) -> int:
    n = len(matrix)

    def solve(r, c, n, matrix, dp):
        leftd, rightd, bottom = float('inf'), float('inf'), float('inf')

        if c == n or c < 0:
            return float('inf')

        if r == n - 1:
            return matrix[r][c]

        if dp[r][c] != 1e9:
            return dp[r][c]

        leftd = matrix[r][c] + solve(r + 1, c - 1, n, matrix, dp)

        rightd = matrix[r][c] + solve(r + 1, c + 1, n, matrix, dp)

        bottom = matrix[r][c] + solve(r + 1, c, n, matrix, dp)

        dp[r][c] = min(leftd, min(bottom, rightd))

        return dp[r][c]

    res = float('inf')
    # Out of range dp initialization
    dp = [[1e9] * n for _ in range(n)]
    for i in range(n):
        # first row iteration
        res = min(res, solve(0, i, n, matrix, dp))

    return res

# Tabulation


def min_fall_path_tabulation(matrix: List[List[int]]) -> int:
    n = len(matrix)
    dp = [[1e9] * n for _ in range(n)]
    # populating first row as it is
    for i in range(n):
        dp[0][i] = matrix[0][i]

    for i in range(1, n):
        for j in range(n):
            # left, right, bottom
            leftd, rightd, bottom = float('inf'), float('inf'), float('inf')
            if i - 1 >= 0 and j - 1 >= 0:
                leftd = matrix[i][j] + dp[i - 1][j - 1]
            if i - 1 >= 0 and j + 1 < n:
                rightd = matrix[i][j] + dp[i - 1][j + 1]
            if i - 1 < n:
                bottom = matrix[i][j] + dp[i - 1][j]

            dp[i][j] = min(leftd, rightd, bottom)

    return min(dp[i])

# Space Optimization


def min_fall_path_spaceop(matrix: List[List: int]) -> int:
    n = len(matrix)
    dp = [None] * n
    # populating first row as it is
    for i in range(n):
        dp[i] = matrix[0][i]

    for i in range(1, n):
        tmp = [0] * n
        for j in range(n):
            # left, right, bottom
            leftd, rightd, bottom = float('inf'), float('inf'), float('inf')
            if i - 1 >= 0 and j - 1 >= 0:
                leftd = matrix[i][j] + dp[j - 1]
            if i - 1 >= 0 and j + 1 < n:
                rightd = matrix[i][j] + dp[j + 1]
            if i - 1 < n:
                bottom = matrix[i][j] + dp[j]

            tmp[j] = min(leftd, rightd, bottom)
        dp = tmp

    return min(dp)


if __name__ == '__main__':
    func = min_fall_path_spaceop
    print(func([[-19, 57], [-40, -5]]))
