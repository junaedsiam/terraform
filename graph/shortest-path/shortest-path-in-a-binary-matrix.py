"""
Problem URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
---------

Problem Description:
---------
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

"""
from queue import Queue


def shortest_path_in_a_binary_matrix(grid):
    if grid[0][0] != 0:
        return -1

    n = len(grid)
    distance = [[float('inf')] * n for _ in range(n)]
    q = Queue()
    q.put((0, 0))
    distance[0][0] = 1
    # 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                  (1, 1), (1, 0), (1, -1), (0, -1)]

    while q.qsize():
        x, y = q.get()
        d = distance[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n or grid[nx][ny] != 0:
                continue

            if d + 1 < distance[nx][ny]:
                distance[nx][ny] = d + 1
                q.put((nx, ny))

    dest = distance[n - 1][n - 1]

    return -1 if dest == float('inf') else dest


if __name__ == '__main__':
    print(shortest_path_in_a_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
