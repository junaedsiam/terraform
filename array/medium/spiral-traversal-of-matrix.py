"""
Problem Statement: Given a Matrix, print the given matrix in spiral order.

Examples:

Example 1:
Input: Matrix[][] = [[ 1, 2, 3, 4 ],
		      [ 5, 6, 7, 8 ],
		      [ 9, 10, 11, 12 ],
	              [ 13, 14, 15, 16 ] ]

Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.

Example 2:
Input: Matrix[][] = [ [ 1, 2, 3 ],
	              [ 4, 5, 6 ],
		      [ 7, 8, 9 ] ]
			    
Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
Explanation: The output of matrix in spiral form.
"""


def spiral_traversal(mat):
    # Time complexity: O(m * n), Space complexity: O(n)
    m = len(mat)
    n = len(mat[0])
    left = 0
    right = n - 1
    top = 0
    bottom = m - 1
    ls = []
    # Maybe have to modify later
    while left < n and top < m:
        for j in range(left, right + 1):
            ls.append(mat[top][j])
        top += 1
        for i in range(top, bottom + 1):
            ls.append(mat[i][right])
        right -= 1
        for j in range(right, left - 1, -1):
            ls.append(mat[bottom][j])
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            ls.append(mat[i][left])
        left += 1
    return ls


if __name__ == '__main__':
    nums1, nums2 = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]],  [[1, 2, 3],
                                         [4, 5, 6],
                                         [7, 8, 9]]
    print(spiral_traversal(nums1))
    print(spiral_traversal(nums2))
