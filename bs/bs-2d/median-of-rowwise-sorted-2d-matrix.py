"""
Problem description: 
---------
Most asked coding interview problem: Median of Row Wise Sorted Matrix

Problem Statement: Given a row-wise sorted matrix of size r*c, where r is no. of rows and c is no. of columns, find the median in the given matrix.

Assume - r*c is odd

Examples:
----------
Example 1:
-------
Input: 
r = 3 , c = 3
1 4 9 
2 5 6
3 8 7
Output: Median = 5
Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9
So, median = 5

Example 2:
--------
Input: 
r = 3 , c = 3
1 3 8
2 3 4
1 2 5
Output: Median = 3
Explanation: If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8
So, median = 3
-------
Problem Constraints:
----
1 <= N, M <= 10^5
1 <= N*M <= 10^6
1 <= A[i] <= 10^9

N*M is odd
"""


def get_less_than_eq_count(nums, target):
    m = len(nums)
    low = 0
    high = m - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return int(low)


def median_of_rowwise_sorted_2d_matrix(mat):
    # Time complexity:
    low = 1
    high = 1e9
    n = len(mat)
    m = len(mat[0])
    while low <= high:
        mid = (low + high) // 2
        count = 0
        for i in range(n):
            count += get_less_than_eq_count(mat[i], mid)
        if count <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return int(low)


if __name__ == '__main__':
    ex_1, ex_2 = [[1, 4, 9],
                  [2, 5, 6], [3, 7, 8]], [[1, 3, 8],
                                          [2, 3, 4],
                                          [1, 2, 5]]
    print(median_of_rowwise_sorted_2d_matrix(ex_1))
    print(median_of_rowwise_sorted_2d_matrix(ex_2))
