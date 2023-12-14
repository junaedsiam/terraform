"""
Problem description: 
---------
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""


def dfs(board, i, j):
    m = len(board)
    n = len(board[0])
    if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
        return
    board[i][j] = '#'

    dfs(board, i + 1, j)
    dfs(board, i - 1, j)
    dfs(board, i, j + 1)
    dfs(board, i, j - 1)


def surrounded_regions(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # Idea is to first find and mark non-flippable 'O' regions and mark them as '#'
    # Finally the matrix will be left with all the 'X' and flippable 'O'
    # Find and flip all the 'O' to 'X' and '#' to 'O'
    m = len(board)
    n = len(board[0])
    # col boundary
    for i in range(n):
        if board[0][i] == 'O':
            dfs(board, 0, i)
        if board[m - 1][i] == 'O':
            dfs(board, m-1, i)
    # row boundary
    for i in range(m):
        if board[i][0] == 'O':
            dfs(board, i, 0)
        if board[i][n - 1] == 'O':
            dfs(board, i, n - 1)

    # flip O to X first
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == '#':
                board[i][j] = 'O'


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    surrounded_regions(board)

    print(board)
