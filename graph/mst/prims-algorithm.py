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
from queue import PriorityQueue


def prims_algorithm(v, adj):
    # code here
    # visited array
    # priority queue
    vis = [0] * v

    q = PriorityQueue()
    q.put((0, 0))
    res = 0

    while q.qsize():
        w, node = q.get()

        if vis[node]:
            continue

        vis[node] = 1
        res += w
        for adj_node, weight in adj[node]:
            if not vis[adj_node]:
                q.put((weight, adj_node))

    return res


if __name__ == '__main__':
    print(prims_algorithm(3,  [[[1, 5], [2, 1]],
          [[0, 5], [2, 3]], [[1, 3], [0, 1]]]))
