"""
Problem description: 
---------
 Given an m*n 2D matrix and an integer, write a program to find if the given integer exists in the matrix.

Given matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row
Example 1:

Input: matrix = 
[[1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]], 

target = 3

Output: true

Explanation: As the given integer(target) exists in the given 2D matrix, the function has returned true.
Example 2:

Input: matrix = 
[[1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]], 

target = 13

Output: false

Explanation: As the given integer(target) does not exist in the given 2D matrix, the function has returned false.
"""


def search_in_a_sorted_2d_matrix(mat, target):
    # Time complexity: O (log(m * n)), Space complexity: O(1)
    row_len = len(mat)
    col_len = len(mat[0])
    low = 0
    high = row_len * col_len - 1

    while low <= high:
        mid = (low + high) // 2
        # Formula: mat[mid/col_len][mid%col_len]
        if mat[mid // col_len][mid % col_len] == target:
            return True
        elif mat[mid // col_len][mid % col_len] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == '__main__':
    ex_1, ex_2 = ([[1, 3, 5, 7],
                   [10, 11, 16, 20],
                   [23, 30, 34, 60]], 3), ([[1, 3, 5, 7],
                                            [10, 11, 16, 20],
                                            [23, 30, 34, 60]], 13)
    print(search_in_a_sorted_2d_matrix(ex_1[0], ex_1[1]))
    print(search_in_a_sorted_2d_matrix(ex_2[0], ex_2[1]))
