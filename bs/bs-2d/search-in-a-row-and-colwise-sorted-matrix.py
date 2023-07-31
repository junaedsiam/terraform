"""
Problem description: 
---------
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
-------
Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
--------
Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""


def search_in_a_row_and_colwise_sorted_matrix(mat, target):
    # Time complexity: O (n)
    """
    Explanation: We could take up to n steps moving left in the first row if target is smaller than all elements in row 1. 
    We could then take up to n steps moving down each column if target is still not found.
    Therefore, the maximum iterations is n + n = 2n
    """
    row_len = len(mat)
    col_len = len(mat[0])
    i = 0
    j = col_len - 1

    while i < row_len and j >= 0:
        if mat[i][j] == target:
            return True
        elif mat[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    ex_1, ex_2 = ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5), ([
        [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
    search_in_a_row_and_colwise_sorted_matrix()
