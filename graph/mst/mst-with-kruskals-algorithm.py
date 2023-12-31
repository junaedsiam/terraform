"""
Problem URL: https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
---------

Problem Description:
---------
Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree. Given adjacency list adj as input parameters . Here adj[i] contains vectors of size 2, where the first integer in that vector denotes the end of the edge and the second integer denotes the edge weight.

 

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5
Explanation:
Only one Spanning Tree is possible
which has a weight of 5.
 

Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function spanningTree() which takes a number of vertices V and an adjacency list adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. Here adj[i] contains vectors of size 2, where the first integer in that vector denotes the end of the edge and the second integer denotes the edge weight.

Expected Time Complexity: O(ElogV).
Expected Auxiliary Space: O(V2).
 

Constraints:
2 ≤ V ≤ 1000
V-1 ≤ E ≤ (V*(V-1))/2
1 ≤ w ≤ 1000
The graph is connected and doesn't contain self-loops & multiple edges.

"""


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find_upar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


def mst_with_kruskals_algorithm(V, adj):
    edges = []
    for i in range(V):
        for it in adj[i]:
            adj_node, wt = it[0], it[1]
            node = i
            edges.append((wt, (node, adj_node)))

    ds = DisjointSet(V)
    edges.sort()
    mst_wt = 0
    for wt, uv in edges:
        u, v = uv[0], uv[1]
        if ds.find_upar(u) != ds.find_upar(v):
            mst_wt += wt
            ds.union_by_size(u, v)

    return mst_wt


if __name__ == '__main__':
    print(mst_with_kruskals_algorithm(3, [[[1, 5], [2, 1]],
          [[0, 5], [2, 3]], [[1, 3], [0, 1]]]))
