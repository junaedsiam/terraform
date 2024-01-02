"""
Problem URL: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
---------

Problem Description:
---------
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.

"""


from typing import List


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find_uparent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_uparent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_uparent(u)
        ulp_v = self.find_uparent(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


def most_stones_removed_with_same_row_or_col(stones: List[List[int]]) -> int:
    n = len(stones)
    max_row, max_col = float('-inf'), float('-inf')
    # As row, col numbers are not given, we have to find it
    # by scanning the stone list
    for row, col in stones:
        max_row = max(row, max_row)
        max_col = max(col, max_col)

    ds = DisjointSet(max_row + max_col + 1)
    # Core concept of the solution is
    # we will consider each row and each col as a node
    # of a graph. We will connect them with the given stone coordinates.
    # There is one catch,
    # row and col both starts with 0, so there will always be an overlap
    # To avoid this, we can add extra padding with col position
    # col = col + max_row + 1
    # This padding will prevent the overlap
    for u, v in stones:
        v_with_pad = v + max_row + 1
        ds.union_by_size(u, v_with_pad)

    cnt = 0

    for i in range(max_row + max_col + 1):
        # Here we find the valid ultimate parents
        # by checking both parent is parent itself, and size > 1
        if ds.parent[i] == i and ds.size[i] > 1:
            cnt += 1

    return n - cnt


if __name__ == '__main__':
    print(most_stones_removed_with_same_row_or_col(
        [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
