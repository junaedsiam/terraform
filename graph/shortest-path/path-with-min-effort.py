"""
Problem URL:https://leetcode.com/problems/path-with-minimum-effort/ 
---------

Problem Description:
---------
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

"""
from queue import PriorityQueue


def path_with_min_effort(heights):
    # shortest path with priority queue
    r = len(heights)
    c = len(heights[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    efforts = [[float('inf')] * c for _ in range(r)]

    q = PriorityQueue()
    q.put((0, (0, 0)))

    while q.qsize():
        effort, coord = q.get()
        x, y = coord

        if (x == r - 1 and y == c - 1):
            return effort

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            new_effort = max(abs(heights[x][y] - heights[nx][ny]), effort)

            if new_effort < efforts[nx][ny]:
                efforts[nx][ny] = new_effort
                q.put((new_effort, (nx, ny)))

    return 0


if __name__ == '__main__':
    print(path_with_min_effort([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
          1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
    print(path_with_min_effort([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
