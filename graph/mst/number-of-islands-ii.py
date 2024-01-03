"""
Problem URL: https://www.codingninjas.com/studio/problems/largest-island_840701
---------

Problem Description:
---------
You are given two integers 'n' and 'm', the dimensions of a grid. The coordinates are from (0, 0) to (n - 1, m - 1).



The grid can only have values 0 and 1.



The value is 0 if there is water and 1 if there is land.



An island is a group of ‘1’s such that every ‘1’ has at least another ‘1’ sharing a common edge.



You are given an array 'queries' of size 'q'.



Each element in 'queries' contains two integers 'x' and 'y', referring to the coordinates in the grid.



Initially, the grid is filled with 0, which means only water and no land.



At each query, the value of 'grid' at (x, y) becomes 1, which means it becomes land.



Find out, after each query, the number of islands in the grid.



Example :
Input: 'n' = 3, 'm' = 4
'queries' = [[1, 1], [1, 2], [2, 3]]

Output: [1, 1, 2]

Explanation:

Initially, the grid was:
0 0 0 0
0 0 0 0
0 0 0 0

After query (1, 1):
0 0 0 0
0 1 0 0
0 0 0 0
There is one island having land (1, 1).

After query (1, 2):
0 0 0 0
0 1 1 0
0 0 0 0
Since (1, 1) and (1, 2) share a common edge, they form one island. So there is one island having lands (1, 1) and (1, 2).

After query (2, 3):
0 0 0 0
0 1 1 0
0 0 0 1
Now there are two islands, one having lands (1, 1) and (1, 2), and another having land (2, 3).

So the number of islands after each query is [1, 1, 2].

"""
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        u_parent = self.findUltimateParent(u)
        v_parent = self.findUltimateParent(v)

        if u_parent == v_parent:
            return

        if u_parent < v_parent:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        else:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]


def number_of_islands_ii(n: int, m: int, queries: List[List[int]]) -> int:
    # Write your code here.
    ds = DisjointSet(n * m)
    res = []
    vis = [[0] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    counter = 0

    for coord in queries:
        u, v = coord
        if vis[u][v]:
            # for repeat we have to also append the same result
            res.append(counter)
            continue

        counter += 1
        vis[u][v] = 1

        for dx, dy in directions:
            nx, ny = u + dx, v + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m or vis[nx][ny] != 1:
                continue

            node_1 = u * m + v
            node_2 = nx * m + ny

            if ds.findUltimateParent(node_1) != ds.findUltimateParent(node_2):
                ds.unionBySize(node_1, node_2)
                counter -= 1

        res.append(counter)

    return res


if __name__ == '__main__':
    print(number_of_islands_ii(3, 4, [[1, 1], [1, 2], [2, 3]]))
