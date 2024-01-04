"""
Problem URL: https://leetcode.com/problems/making-a-large-island/description/
---------

Problem Description:
---------
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

"""


from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        u_parent = self.findUltimateParent(u)
        v_parent = self.findUltimateParent(v)

        if u_parent == v_parent:
            return

        if u_parent < v_parent:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        else:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]


def isInvalid(nx, ny, grid):
    n = len(grid)
    if nx < 0 or ny < 0 or nx >= n or ny >= n or grid[nx][ny] != 1:
        return True
    return False


def genNodeVal(i, j, n):
    return i * n + j


def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    visited = [[0] * n for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ds = DisjointSet(n * n)
    # first generate the disjoint set from the given grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] and not visited[i][j]:
                visited[i][j] = 1
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if isInvalid(nx, ny, grid):
                        continue
                    ds.unionBySize(
                        genNodeVal(
                            i, j, n), genNodeVal(nx, ny, n)
                    )
    res = 0
    # traverse through the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                val = 0
                s = set()
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if isInvalid(nx, ny, grid):
                        continue
                    s.add(ds.findUltimateParent(
                        genNodeVal(nx, ny, n)))

                for item in s:
                    val += ds.size[item]

                res = max(res, val + 1)
    # In case the whole grid is full of 1
    for i in range(n * n):
        res = max(res, ds.size[ds.findUltimateParent(i)])

    return res


if __name__ == '__main__':
    print(largestIsland([[1, 1], [1, 0]]))
    print(largestIsland([[1, 1], [1, 1]]))
