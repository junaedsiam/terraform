"""
Problem description: 
---------
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
from queue import Queue


def zero_one_matrix(mat):
    m = len(mat)
    n = len(mat[0])
    q = Queue()
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Cells contain zeroes are nearest of themselves, so put them in queue first
    # and all the one cells will be marked as -1, and we will visit them one by one

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.put((i, j))
            else:
                mat[i][j] = -1

    while q.qsize():
        x, y = q.get()
        for nx, ny in dir:
            cx, cy = x + nx, y + ny
            if cx >= 0 and cy >= 0 and cx < m and cy < n and mat[cx][cy] == -1:
                mat[cx][cy] = mat[x][y] + 1
                q.put((cx, cy))

    return mat


if __name__ == '__main__':
    print(zero_one_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
