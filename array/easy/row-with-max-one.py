"""
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).
"""


def row_with_max_ones(mat):
    """
    The idea is a little unique, but not very hard to grasp. 
    You have to traverse through each row from the beginning, 
    and you will mark the highest index of that row.
    Now you don't have to check lesser than that index value for next rows. 
    You only have to check higher values from that index to find the max 1 row.
    -------
    Time complexity: O(m + n), Space complexity: O(1)
    """
    row = len(mat)
    col = len(mat[0])
    max_row_index = -1
    index = col-1
    for i in range(0, row):
        while (index >= 0 and mat[i][index] == 1):
            max_row_index = i
            index -= 1
    return max_row_index


if __name__ == '__main__':
    mat = [[0, 0, 0, 0],
           [0, 1, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
    print(row_with_max_ones(mat))
