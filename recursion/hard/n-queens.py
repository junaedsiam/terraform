"""
Problem description: 
---------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""


def is_safe(row, col, board):
    # A Queen can cover 8 sides
    # 1. row-- (top),
    # 2. row++ (bottom),
    # 3. col-- (left),
    # 4. row--, col-- (top left diagonal),
    # 5. row++, col-- (bottom left diagonal)
    # 6. row--, col++ (top right diagonal)
    # 7. col++ (right)
    # 8. row++, col++ (bottom right diagonal)
    #####
    # But if we go from left to right we do not have to check all 8.
    # If we check only
    # 4. row--, col-- (top left diagonal)
    # 3. col-- (left),
    # 5. row++, col-- (bottom left diagonal)
    # It will suffice
    cache_row = row
    cache_col = col

    # Top left diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    row = cache_row
    col = cache_col
    # Left
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row = cache_row
    col = cache_col
    # bottom left diagonal
    while row < len(board) and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1
    return True


def solve(col, ans, board, n):
    if col == n:
        ans.append(board.copy())
        return
    for row in range(n):
        if is_safe(row, col, board):
            board[row] = board[row][0:col] + 'Q' + board[row][col + 1:]
            solve(col + 1, ans, board, n)
            board[row] = board[row][0:col] + '.' + board[row][col + 1:]


def n_queens(n):
    ans = []
    board = ['.' * n for _ in range(n)]
    solve(0, ans, board, n)
    return ans


if __name__ == '__main__':
    print(n_queens(4))
    print(n_queens(1))
