"""
Problem URL: https://leetcode.com/problems/unique-paths-ii/
---------

Problem Description:
---------
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

"""
# This problem is exactly same as unique-paths problem with slight modification
# So there will be only tabulation implementation for this. You can get other types
# of implementations from unique-paths file.
from typing import List


def unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> int:
    # Tabulation
    # Time complexity: O(m * n)
    # Space Complexity: O(m * n)
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if obstacleGrid[r][c] == 1:
                dp[r][c] = 0
                continue
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


if __name__ == '__main__':
    print(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
