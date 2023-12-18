"""
Problem description: 
---------

"""


def dfs(row, col, row_start, col_start, arr, tmp):
    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]) or arr[row][col] != 1:
        return
    # marking it visited
    arr[row][col] = 0
    tmp.append((row - row_start, col - col_start))
    dfs(row - 1, col, row_start, col_start, arr, tmp)
    dfs(row + 1, col, row_start, col_start, arr, tmp)
    dfs(row, col + 1, row_start, col_start, arr, tmp)
    dfs(row, col - 1, row_start, col_start, arr, tmp)


def distinct_islands(arr, m, n):
    # Write your code here.
    s = set()

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                tmp = []
                dfs(i, j, i, j, arr, tmp)
                s.add(tuple(tmp))

    return len(s)


if __name__ == '__main__':
    ls = [[1, 1, 0, 1, 1],
          [1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1],
          [1, 1, 0, 1, 1]]
    print(distinct_islands(ls, len(ls), len(ls[0])))
