"""
Problem description: 
---------
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.

"""


def dfs(grid, row, col):
    m = len(grid)
    n = len(grid[0])
    if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] != 1:
        return

    grid[row][col] = '#'

    dfs(grid, row - 1, col)
    dfs(grid, row + 1, col)
    dfs(grid, row, col - 1)
    dfs(grid, row, col + 1)


def number_of_enclaves(grid):
 # Traverse the boundaries
    m = len(grid)
    n = len(grid[0])

    # col boundary
    for i in range(n):
        if grid[0][i] == 1:
            dfs(grid, 0, i)
        if grid[m - 1][i] == 1:
            dfs(grid, m - 1, i)

    # row boundary
    for i in range(m):
        if grid[i][0] == 1:
            dfs(grid, i, 0)
        if grid[i][n - 1] == 1:
            dfs(grid, i, n-1)

    # count the 1
    counter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                counter += 1

    return counter


if __name__ == '__main__':
    print(number_of_enclaves(
        [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
