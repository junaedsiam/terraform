"""
Problem description: 
---------
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
---------------
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
--------------
EXAMPLE: 1
---
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
-------
EXAMPLE: 2
---
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
"""


def get_max_element_index(nums):
    max_index = 0
    for i in range(len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index


def find_peak_element_in_2d_matrix(matrix):
    n = len(matrix)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        max_idx = get_max_element_index(matrix[mid])
        if mid == 0:
            if matrix[mid][max_idx] > matrix[mid + 1][max_idx]:
                return [mid, max_idx]
        if mid == n - 1:
            if matrix[mid][max_idx] > matrix[mid - 1][max_idx]:
                return [mid, max_idx]
        if matrix[mid][max_idx] > matrix[mid + 1][max_idx] and matrix[mid][max_idx] > matrix[mid - 1][max_idx]:
            return [mid, max_idx]
        if matrix[mid][max_idx] < matrix[mid + 1][max_idx]:
            low = mid + 1
        else:
            high = mid - 1
    return [-1, -1]


if __name__ == '__main__':
    ex_1, ex_2, ex_3 = [[1, 4], [3, 2]], [[10, 20, 15], [21, 30, 14], [7, 16, 32]], [
        [11, 27, 32, 31, 14], [10, 4, 11, 25, 1], [25, 17, 30, 19, 28]]
    print(find_peak_element_in_2d_matrix(ex_1))
    print(find_peak_element_in_2d_matrix(ex_2))
    print(find_peak_element_in_2d_matrix(ex_3))
