"""
Problem description: 
---------
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""


def solve(i, j, idx, board, word):
    if idx == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
        return False
    # mark visited
    board[i][j] = '0'

    is_found = solve(i - 1, j, idx + 1, board, word) or \
        solve(i + 1, j, idx + 1, board, word) or \
        solve(i, j - 1, idx + 1, board, word) or \
        solve(i, j + 1, idx + 1, board, word)
    # Reset back to previous for other searches (backtrack)
    board[i][j] = word[idx]

    return is_found


def word_search(board, word):
    # Time complexity:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and solve(i, j, 0, board, word):
                return True

    return False


if __name__ == '__main__':
    ex_1, ex_2, ex_3 = [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"], [[["A", "B", "C", "E"], [
        "S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"], [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"]
    print(word_search(ex_1[0], ex_1[1]))
    print(word_search(ex_2[0], ex_2[1]))
    print(word_search(ex_3[0], ex_3[1]))
