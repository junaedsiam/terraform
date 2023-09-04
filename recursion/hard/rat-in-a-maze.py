"""
Problem description: 
---------
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Your Task:  
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1
"""


def solve(row, col, path, ans, matrix, n):
    if row < 0 or col < 0 or row == n or col == n:
        return
    if matrix[row][col] == 0:
        return
    if row == n - 1 and col == n - 1:
        ans.append(path)
        return

    # mark visited
    matrix[row][col] = 0
    # down
    solve(row + 1, col, path+'D', ans, matrix, n)
    # right
    solve(row, col + 1, path + 'R', ans, matrix, n)
    # up
    solve(row - 1, col, path + 'U', ans, matrix, n)
    # left
    solve(row, col - 1, path + 'L', ans, matrix, n)
    # backtrack
    matrix[row][col] = 1


def rat_in_a_maze(matrix):
    ans = []
    row, col = 0, 0
    solve(row, col, "", ans, matrix, len(matrix))
    return ans


if __name__ == '__main__':
    ex_1, ex_2 = [], []
    rat_in_a_maze()
