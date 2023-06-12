"""
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

Examples
Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
"""
# Brute force: traverse the matrix, and if 0 has been found in i,j position
# then mark the corresponding row and column with -1 value
# Why -1 ? If we start setting zeroes in the same traversal for the whole row and column of that element
# those zeroes will be treated same as initial zero. But we do not want that.
# So after finishing the first traversal, we will traverse again to make all the -1 -> 0
# Time complexity: O((N*M)*(N + M)) + O(N*M) , Space complexity: O(1)


def set_matrix_zeros(mat):
    # Better approach, using row col hashing
    # Time complexity: O(2 * m * n), Space complexity: O(m + n)
    m = len(mat)
    n = len(mat[0])
    row = [0] * m
    col = [0] * n
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                mat[i][j] = 0


def set_matrix_zeros_optimal(mat):
    # In this optimal approach we will boil down the space complexity to constant space.
    m = len(mat)
    n = len(mat[0])
    col0 = mat[0][0]
    for i in range(m):
        for j in range(n):
            # Instead of taking extra extra hash array, we will first column as a hash for the rows
            # And first row as a hash for the columns
            # with an overlap at i,j = 0,0. To solve the overlap, we will have a variable col0 to store the column 0 hash
            if mat[i][j] == 0:
                if i == 0:
                    col0 = 0
                else:
                    mat[0][j] = 0
                mat[i][0] = 0
    # Then we will start iterating from the end to start except the first row and column.
    # We will evaluate first row and column seperately
    for i in range(m - 1, 0, -1):
        for j in range(n - 1, 0, -1):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    # Now go through the first row
    if mat[0][0] == 0:
        for j in range(n):
            mat[0][j] = 0

    # And finally go through the first column
    # order matters here as row contains col hash, and we are storing column 0 hash at col0
    if col0 == 0:
        for i in range(m):
            mat[i][0] = 0


if __name__ == '__main__':
    func = set_matrix_zeros_optimal
    nums1, nums2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [
        [0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    func(nums1)
    print(nums1)
    func(nums2)
    print(nums2)
