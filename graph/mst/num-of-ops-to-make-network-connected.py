"""
Problem URL: https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
---------

Problem Description:
---------
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.

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


def num_of_ops_to_make_network_connected(n: int, connections: List[List[int]]) -> int:
    dis = DisjointSet(n)
    extra_edges = 0

    for u, v in connections:
        if dis.find_uparent(u) == dis.find_uparent(v):
            # If u,v already has a common parent, there is no need
            # to connect them again, so the edge is extra
            extra_edges += 1
        else:
            dis.union_by_size(u, v)

    left = 0

    for i in range(n):
        # If the node's parent is the node itself, meaning that node is
        # not connected yet
        if dis.parent[i] == i:
            left += 1
    # N nodes require N - 1 edge
    required_edges = left - 1

    if extra_edges >= required_edges:
        return required_edges

    return -1


if __name__ == '__main__':
    print(num_of_ops_to_make_network_connected(
        6,  [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
