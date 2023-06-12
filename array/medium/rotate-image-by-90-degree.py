"""
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
Example 1:

Input: 
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.

Example 2:

Input: [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

Output:[
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
]

Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix
"""
"""
 [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],   -> transpose -> reverse each column -> You get 90 degree clockwise rotation
    [15,14,12,16]
]
"""


def rotate_image_by_90_deg(mat):
    m = len(mat)
    n = len(mat[0])
    # Transpose the matrix, make row -> col and col -> row
    for i in range(m):
        # Take a closer look here. Its not range(n), its range(i)
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(m):
        mat[i].reverse()


if __name__ == '__main__':
    nums1, nums2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],  [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    rotate_image_by_90_deg(nums1)
    print(nums1)
    rotate_image_by_90_deg(nums2)
    print(nums2)
